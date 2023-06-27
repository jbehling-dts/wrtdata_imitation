from flask import render_template
from . import user_bp

@user_bp.route('/users')
def index():
    return render_template('users.html')
