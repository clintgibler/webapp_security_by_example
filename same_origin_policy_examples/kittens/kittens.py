from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request, session, flash, send_file
from flask import make_response # for setting cookies
import flask
import os
import subprocess
import ipdb

from routes import *

app = Flask(__name__)

##############
# Index page #
##############

@app.route("/")
def index():
    return render_template("index.html")

#################
# Server config #
#################

app.secret_key = '0mG_So#S3kreT-4nd_unGuEss4ble'

app.config.update(
    SESSION_COOKIE_HTTPONLY = False
)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    app.debug = True
    app.run(port=5001)
