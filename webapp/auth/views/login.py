from .. import auth
from flask import render_template, redirect, url_for, flash, request
from ..forms import LoginForm
from flask_login import login_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        from ...models.user import User
        user = User.query.filter_by(email=form.email.data).one()
        if user is not None and (user.check_password(form.password.data)):
            # login user and remember_me cookie session
            if user:
                login_user(user, form.remember.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        else:
            flash('Invalid username or password')
    
    return render_template('auth/login.html', form=form, remember=True)