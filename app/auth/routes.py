from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import LoginForm, SignUpForm
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('main.homepage'))

@auth.route('/signup')
def signup():
    form = SignUpForm()

    
    return render_template('signup.html')