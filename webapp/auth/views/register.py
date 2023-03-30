from .. import auth
from ... import db
from flask import render_template, flash, url_for, redirect
from ..forms import RegisterForm

from flask_login import login_user, login_required, logout_user


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    from ...models.user import User
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password='', about_me='', institution='')
        #set password to bcrypt hash
        user.set_password(password=form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Registration successful Login to continue')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)
