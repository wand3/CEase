from .. import auth
from flask import render_template, redirect, url_for, flash
from ..forms import LoginForm
from ...models.user import *
from flask_login import login_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user, remember=form.remember.data)
        flash("You have been logged in.", category="success")
        return redirect(url_for('main.index'))
    
    return render_template('auth/login.html')