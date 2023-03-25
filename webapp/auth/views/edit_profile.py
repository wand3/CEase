from .. import auth
from flask import render_template

@auth.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    
    return render_template('auth/edit_profile.html')