from flask import Flask
from flask import render_template
from flask import request, session, flash, send_file
import os
import subprocess

import ipdb

app = Flask(__name__)

##############
# Index page #
##############

@app.route("/")
def index():
    return render_template("index.html")

################
# XSS Examples #
################

# Each of these @app.route() lines define the ("controller")
# code that will be run when that page is loaded.
#
# The first argument to render_template is the name of the
# template that will be rendered, that is, the basis for the
# HTML that will be returned to the user when the page loads.
#
# The second argument specifies variables that are passed to
# the template. Look in templates/hello_html.html and notice
# how the variable "name" is inserted twice. Variables in
# Jinja, the library Flask uses by default for page
# templates, are inserted like: {{ var_name }}.
#
# So how does the variable "name" in hello_html.html get
# its value? In the assignment in the second argument:
#     name = request.args.get('name', '_name_not_specified_')
#
# The above means that the "name" variable in the template is
# set to:
#     request.args.get('name', '<name not specified>')
# `request.args.get`` extracts an argument from the URL
# parameters, which for GET requests, are provided like:
#    http://example.com/index?arg1=foo&arg2=bar
# In this example, the index page was provided two arguments,
# "arg1" which will have the value "foo", and "arg2" will be
# "bar".
#
# To provide the "name" URL parameter for this endpoint,
# try navigating to:
#      http://localhost:5000/hello_html?name=Ada
@app.route('/hello_html/')
def hello_html():
    return render_template("hello_html.html", name=request.args.get('name', '_name not specified_'))

# Note here that the URL parameter "style" is being
# extracted, not "name" this time.
@app.route('/hello_html_attr/')
def hello_html_attr():
    return render_template("hello_html_attr.html",
                           style=request.args.get('style', 'color:blue'))

# You know what param is being accessed here :)
@app.route('/hello_js/')
def hello_js():
    return render_template("hello_js.html",
                           username=request.args.get('username', 'GrumpyCat'))

##########################
# Client side validation #
##########################

# 1. secrets in HTML
# 2. AJAX request that loads passwords locally and compares
# 3. Do comparison locally (mathy function) and sends "success=true" to server
#    - muck with JS
# 4. Rely on header value (view server source, above don't)

# Show danger of having a state-changing request be both GET and POST

@app.route('/client_side/login_one/')
def client_side_login_one():
    return render_template("client_side/login_one.html")

@app.route('/client_side/login_two/')
def client_side_login_two():
    return render_template("client_side/login_two.html")

@app.route('/client_side/login_three/')
def client_side_login_three():
    return render_template("client_side/login_three.html")

@app.route('/client_side/login_four/')
def client_side_login_four():
    return render_template("client_side/login_four.html")

@app.route('/validate_email/')
def hello_validate_email():
    return render_template("validate_email.html")

@app.route('/hello_dropdown/', methods=['GET', 'POST'])
def hello_dropdown():
    if request.method == 'POST':
        known_movies = ["matrix", "hackers", "sneakers"]
        movie = request.form['movie']

        if movie in known_movies:
            flash(movie + " is awesome but I know that one. Got anything new?")
        else:
            flash("Nice work! I'll check it out")

    return render_template("hello_dropdown.html")

@app.route('/exfil/')
def hello_exfil():
    session['user_email'] = "joebob@somewhere.com"
    return render_template("exfil.html",
                           username=request.args.get('username', '[enter user name]'))

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
    app.run()
