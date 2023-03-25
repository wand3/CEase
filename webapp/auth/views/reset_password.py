from .. import auth
from flask import render_template

@auth.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    
    return render_template('auth/reset_password.html')