from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

main = Blueprint('main', __name__)

bcrypt = Bcrypt(app)


@main.route('/')
def homepage():
    return render_template('homepage.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/logout')
def logout():
    return redirect(url_for('main.homepage'))

@main.route('/signup')
def signup():
    return render_template('signup.html')

@main.route('/beer_submit')
def beer_submit():
    return render_template('beer_submit.html')

@main.route('/beer_review')
def beer_review():
    return render_template('beer_review.html')

@main.route('/beer_detail')
def beer_detail():
    return render_template('beer_detail.html')