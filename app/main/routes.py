from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from app.main.forms import BeerSubmit, BeerReview
from app.models import Beer
from app import app, db

main = Blueprint('main', __name__)

bcrypt = Bcrypt(app)


@main.route('/')
def homepage():
    all_beers = Beer.query.all()

    return render_template('homepage.html', all_beers=all_beers)

@main.route('/beer_submit', methods=['GET', 'POST'])
def beer_submit():
    """ Page for submitting a beer """

    form = BeerSubmit()

    if form.validate_on_submit():
        new_beer = Beer(
            name=form.name.data,
            brand=form.brand.data
        )
        db.session.add(new_beer)
        db.session.commit()

        flash('Beer successfully submitted!')
        #TODO: redirect to beer_detail
        return redirect(url_for('main.beer_detail', beer_id=new_beer.id))

    return render_template('beer_submit.html', form=form)

@main.route('/beer_review/<beer_id>')
def beer_review(beer_id):
    beer = Beer.query.get(beer_id)
    form = BeerReview()

    return render_template('beer_review.html', form=form, beer=beer)

@main.route('/beer_detail/<beer_id>')
def beer_detail(beer_id):
    beer = Beer.query.get(beer_id)

    return render_template('beer_detail.html', beer=beer)
