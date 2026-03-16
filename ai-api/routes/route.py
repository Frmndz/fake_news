from flask import Blueprint
from controllers.welcome import show_welcome

welcome_bp = Blueprint("welcome_bp", __name__)

welcome_bp.route("/")(show_welcome)