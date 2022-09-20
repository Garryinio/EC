from app import app, db
from flask import render_template, redirect, url_for, flash, request, session
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse


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
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Welcome, {}'.format(user.username), "success")
        return redirect(url_for('home'))
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page = url_for('home')
    return render_template('login.html', form=form, title='Login page')


@app.route('/admin_dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
        if user.check_admin():
            return render_template('admin/admin_dashboard.html', title="Admin login page")
        flash("This page is only available for admins!", 'danger')
        return redirect(url_for('home'))
    flash("You're not logged in!", 'danger')
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


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
