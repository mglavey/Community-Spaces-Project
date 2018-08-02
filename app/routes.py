from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import RegistrationForm, LoginForm, AdminForm, CommunityOrganizerForm, CommunitySpaceForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
from werkzeug.urls import url_parse


@app.route('/', methods=['GET', 'POST'])
def index():
    context = {
        "form": RegistrationForm()
    }
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.community_organizer.data:
            return redirect(url_for('register_layout1'))
        if form.community_space.data:
            return redirect(url_for('register_layout2'))
    return render_template('index.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('index', form=form)


@app.route('/register/layout1', methods=['GET', 'POST'])
def register_layout1():
    context = {
        "form": CommunityOrganizerForm()
    }
    return render_template('register/layout1.html', **context)

@app.route('/register/layout2', methods=['GET', 'POST'])
def register_layout2():
    context = {
        "form": CommunitySpaceForm()
    }
    return render_template('register/layout2.html', **context)

@app.route('/homepage/layout1')
def homepage_layout1():
    return render_template('/homepage/layout1')