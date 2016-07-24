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

@app.route("/xss/")
def xss_index():
    return render_template("xss_index.html")

@app.route("/client_side/")
def client_side_index():
    return render_template("client_side_index.html")

######################
# Other common vulns #
######################

@app.route('/path_traversal/')
def path_traversal():
    return render_template("path_traversal.html")

@app.route('/show_file/')
def show_file():
    file = request.args.get("path")
    return open(file).read()

@app.route('/command_injection/')
def command_injection():
    path = request.args.get('path', APP_ROOT)
    filelist = subprocess.check_output("ls " + path, shell=True)

    # subprocess commands returns bytes b'...', need
    # to turn into a string with decode before we can
    # split
    filelist = filelist.decode("utf-8").split("\n")
    return render_template("command_injection.html",
                           path=path, filelist=filelist)

@app.route('/csrf/')
def csrf():
    # TODO
    pass

@app.route('/sqli/')
def sqli():
    # TODO
    pass

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
    app.register_blueprint(routes)
    app.run()
