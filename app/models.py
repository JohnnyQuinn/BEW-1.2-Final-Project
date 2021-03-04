from flask_login import UserMixin
from sqlalchemy.orm import backref
from app import db 

class User(UserMixin, db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(30), nullable=False)

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    brand = db.Column(db.String(20), nullable=False )
    reviews = db.relationship('Review', secondary='beer_review', back_populates='beer')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(30))
    beer = db.relationship('Beer', secondary='beer_review', back_populates='reviews')

beer_review_table = db.Table('beer_review',
    db.Column('beer_id', db.Integer, db.ForeignKey('beer.id')),
    db.Column('review_id', db.Integer, db.ForeignKey('review.id'))
)


