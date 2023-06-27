from flask import Blueprint

# Create a Blueprint for the home-related views
user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static', static_url_path='/user/static')

# Import the views that belong to the home blueprint
from .user import *
