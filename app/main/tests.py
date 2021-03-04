import os 
import unittest

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

class MainTests(unittest.TestCase):

    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def test_homepage_logged_out(self):
        """Test that:
            Displayed on Page: 
                - Log In link
                - Sign Up link
            Not displayed on page:
                - Log Out link
        """

        # Make a GET request
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Check that page contains all of the things we expect
        response_text = response.get_data(as_text=True)
        self.assertIn('Log In', response_text)
        self.assertIn('Sign Up', response_text)

        # Check that the page doesn't contain things we don't expect
        # (these should be shown only to logged in users)
        self.assertNotIn('Log Out', response_text)

    def test_homepage_logged_in(self):
        """Test that: 
            Displayed on page: 
                - Log Out link
            Not displayed on page: 
                - Log In link 
                - Sign Up link
        """
        # Set up
        create_user()
        login(self.app, 'test_user', 'password')

        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response_text = response.get_data(as_text=True)
        self.assertIn('Log Out', response_text)

        self.assertNotIn('Log In', response_text)
        self.assertNotIn('Sign Up', response_text)

    def test_submit_beer(self):
        """
        Test that a beer object is successfully created and submitted
        """
        # Set up
        create_user()
        login(self.app, 'test_user', 'password')

        # POST request with test data
        post_data = {
            'name': 'test beer',
            'brand': 'test brand'
        }
        self.app.post('/beer_submit', data=post_data)

        created_beer = Beer.query.filter_by(name='test beer').one()
        self.assertIsNotNone(created_beer)
        self.assertEqual(created_beer.name, 'test beer')
    
    def test_submit_beer_logged_out(self):
        """
            Test that when a logged out user tries to access the beer_submit page that they are redirected
            to login
        """
        response = self.app.get('/beer_submit')

        self.assertEqual(response.status_code, 302)

