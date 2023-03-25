from .. import auth
from flask import render_template

@auth.route('/change_email', methods=['GET', 'POST'])
def change_email():
    
    return render_template('auth/change_email.html')