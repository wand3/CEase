from .. import auth
from flask import render_template

@auth.route('/register', methods=['GET', 'POST'])
def register():
    
    return render_template('auth/register.html')