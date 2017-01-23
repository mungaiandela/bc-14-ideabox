from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import User

@auth.route('/register', methods=['GET', 'POST'])
def register():
    '''
    handles registration
    adds new users to the database
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
        username = form.username.data,
        first_name= form.first_name.data,
        last_name = form.last_name.data,
        password = form.password.data)

    #commit user to the db

        db.session.add(user)
        db.session.commit()

        flash('Registration successful. Login!')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form, title="Register")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''
    handles login
    logs in existing users from db
    '''
    form = LoginForm()
    if form.validate_on_submit():
        #checks for user in db
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(
        form.password.data):
        #login can now be validated
            login_user(user)
        #redirect

        return redirect(url_for(home.ideabox))

    else:
        flash('Invalid e-mail/Password')

    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    '''
    handles logout
    '''
    logout_user()
    flash('You have logged out. Bye!')

    return redirect(url_for('auth.login'))
