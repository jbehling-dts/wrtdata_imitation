from flask import Blueprint

# Create a Blueprint for the home-related views
home_bp = Blueprint('home', __name__, template_folder='templates')
# Import the views that belong to the home blueprint
from .home import *
