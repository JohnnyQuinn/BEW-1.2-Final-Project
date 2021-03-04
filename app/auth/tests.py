import os
from unittest import TestCase

from app import app, db, bcrypt
from app.models import User, Beer, Review

#################################################
# Setup
#################################################

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def create_user():
    password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='test_user', password=password_hash)
    db.session.add(user)
    db.session.commit()

#################################################
# Tests
#################################################

class AuthTests(TestCase):
    """Tests for authentication (login & signup)."""
    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
    
    def test_signup(self):
        """
            Tests creating a account
        """
        post_data = {
            'username': 'test_user',
            'password': 'password'
        }

        self.app.post('/signup', data=post_data)

        test_user = User.query.filter_by(username='test_user').one()
        self.assertIsNotNone(test_user)
    
    def test_signup_existing_user(self):
        """ 
            Tests attempting to create a account with the same username of an existing account 
        """
        
        #creates user with username 'test_user'
        create_user() 
        
        post_data = {
            'username': 'test_user',
            'password': 'password'
        }
        response = self.app.post('/signup', data=post_data)
        response_text = response.get_data(as_text=True)

        self.assertIn('That username is taken. Please choose a different one.', response_text)
    

