from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


@app.route("/frontend/<path:path>")
def send_assets(path):
    print("build/" + path)
    return send_from_directory('../frontend', "build/" + path)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.mod_auth.controllers import mod_auth as auth_module  # noqa
from app.mod_ecomm.controllers import mod_ecomm as ecomm_module  # noqa

app.register_blueprint(auth_module)
app.register_blueprint(ecomm_module)

db.create_all()
