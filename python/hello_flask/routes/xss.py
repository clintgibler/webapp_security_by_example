from flask import render_template
from . import routes
from flask import request, session, flash, send_file

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
#      http://localhost:5000/xss/hello_html?name=Ada
@routes.route('/xss/hello_html/')
def hello_html():
    return render_template("hello_html.html", name=request.args.get('name', '_name not specified_'))

# Note here that the URL parameter "style" is being
# extracted, not "name" this time.
@routes.route('/xss/hello_html_attr/')
def hello_html_attr():
    return render_template("hello_html_attr.html",
                           style=request.args.get('style', 'color:blue'))

# You know what param is being accessed here :)
@routes.route('/xss/hello_js/')
def hello_js():
    return render_template("hello_js.html",
                           username=request.args.get('username', 'GrumpyCat'))

@routes.route('/xss/exfil/')
def hello_exfil():
    session['user_email'] = "joebob@somewhere.com"
    return render_template("exfil.html",
                           username=request.args.get('username', '[enter user name]'))

