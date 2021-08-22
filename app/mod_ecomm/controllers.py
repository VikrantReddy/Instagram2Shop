from flask import Blueprint, Flask, send_from_directory
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.mod_auth.forms import LoginForm
from app.mod_auth.models import User

mod_ecomm = Blueprint('products', __name__, url_prefix='/products',
                      static_folder='../../frontend/build')


@mod_ecomm.route("/", defaults={'path': ''})
def serve(path):
    if path:
        return send_from_directory(mod_ecomm.static_folder, path)
    else:
        return send_from_directory(mod_ecomm.static_folder, 'index.html')
