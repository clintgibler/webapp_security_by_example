from flask import render_template
from . import routes
from flask import redirect
from flask import url_for
from flask import request, session, flash, send_file
from flask import make_response # for setting cookies
import flask

##########################
# Client side validation #
##########################

@routes.route('/client_side/login_one/')
def client_side_login_one():
    return render_template("client_side/login_one.html")

@routes.route('/client_side/login_one_verify', methods=['POST'])
def client_side_login_one_verify():
    if request.form.get('username') == 'admin' and \
       request.form.get('password') == 'SuperSecureP4ssw0rd':
        flash("Correct! Nicely done.")
    else:
        flash("Incorrect password")

    return redirect(url_for('routes.client_side_login_one'))
###

@routes.route('/client_side/login_two/')
def client_side_login_two():
    return render_template("client_side/login_two.html")

@routes.route('/client_side/login_two_verify', methods=['POST'])
def client_side_login_two_verify():
    mapping = client_side_login_two_known_users()
    username = request.form.get('username')
    password = request.form.get('password')

    if username in mapping.keys() and mapping[username] == password:
        flash("Correct! Nicely done.")
    else:
        flash("Incorrect password")

    return redirect(url_for('routes.client_side_login_two'))

def client_side_login_two_known_users():
    return {"neo": "Th3_0ne",
            "trinity": "Wh1t3_R4bbit"}

@routes.route('/client_side/login_two/known_users')
def client_side_login_two_known_users_api():
    return flask.jsonify(client_side_login_two_known_users())

###

@routes.route('/client_side/login_three/')
def client_side_login_three():
    resp = make_response(render_template("client_side/login_three.html"))
    resp.set_cookie('logged_in', 'false', path='/client_side/login_three')
    return resp

@routes.route('/client_side/login_three_verify', methods=['POST'])
def client_side_login_three_verify():
    if request.cookies.get('logged_in') == "true":
        flash("Correct! Nicely done.")
    else:
        flash("Incorrect password")

    return redirect(url_for('routes.client_side_login_three'))

###

@routes.route('/client_side/login_four/')
def client_side_login_four():
    resp = make_response(render_template("client_side/login_four.html"))
    resp.headers['X-Logged-In'] = 'false'
    return resp

@routes.route('/client_side/login_four_verify', methods=['POST'])
def client_side_login_four_verify():
    if request.headers.get('X-Logged-In') == "true":
        flash("Correct! Nicely done.")
    else:
        flash("Incorrect password")

    resp = make_response(redirect(url_for("routes.client_side_login_four")))
    resp.headers['X-Logged-In'] = 'false'
    return resp

###

# TODO: below

@routes.route('/validate_email/')
def hello_validate_email():
    return render_template("validate_email.html")

@routes.route('/hello_dropdown/', methods=['GET', 'POST'])
def hello_dropdown():
    if request.method == 'POST':
        known_movies = ["matrix", "hackers", "sneakers"]
        movie = request.form['movie']

        if movie in known_movies:
            flash(movie + " is awesome but I know that one. Got anything new?")
        else:
            flash("Nice work! I'll check it out")

    return render_template("hello_dropdown.html")

