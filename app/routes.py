from app import app, db
from flask import render_template, redirect, url_for, flash, request, session
from app.forms import RegistrationForm, LoginForm
from app.models import User, UserInformation
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse


@app.route('/admin_dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
        if user.check_admin():
            return render_template('admin/admin_dashboard.html', title="Admin dashboard")
        flash("This page is only available for admins!", 'danger')
        return redirect(url_for('home'))
    flash("You're not logged in!", 'danger')
    return redirect(url_for('home'))


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', "danger")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Welcome, {}'.format(user.username), "success")
        return redirect(url_for('home'))
    return render_template('login.html', form=form, title='Login page')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/profile')
def profile():
    has_info = UserInformation.query.filter_by(id_user=current_user.id).first()

    has_info_bool = False if has_info is None else True

    # if has_info_bool is True:
    #     has_info = UserInformation.query.filter_by(id_user=1).all()

    user_info = UserInformation.query.filter_by(id_user=1).all() if has_info_bool else None

    is_admin = current_user.check_admin()

    return render_template('profile.html', title='Profile', has_info_bool=has_info_bool, user_info=user_info
                           , is_admin=is_admin)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome {form.name.data}! Thanks for registering!", 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', title='Register user', form=form)


@app.route('/shop')
def shop():
    return render_template('shop.html', title='Shopping')
