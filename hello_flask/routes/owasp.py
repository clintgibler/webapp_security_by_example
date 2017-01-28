from flask import render_template
from . import routes
from flask import request, session, flash, send_file, redirect, url_for
import os
import subprocess

@routes.route('/owasp/path_traversal/')
def owasp_path_traversal():
    base_dir = "static"
    files = os.listdir(base_dir)

    current_file = request.args.get("current_file")

    if current_file:
        current_file = os.path.join(base_dir,current_file)

    if current_file and os.path.isfile(current_file):
        file_content = open(current_file).read()
    else:
        file_content = "Couldn't find file: %s" % current_file

    return render_template("owasp/path_traversal.html", files=files,
                           current_file=current_file, file_content=file_content)

@routes.route('/owasp/command_injection/')
def owasp_command_injection():
    directory = request.args.get('directory', 'static')
    cmd_output = subprocess.check_output("ls " + directory, shell=True)
    files_str = cmd_output.decode('ascii') # convert to normal string
    files = [f for f in files_str.split("\n") if f != ""]
    return render_template("owasp/command_injection.html", directory=directory, files=files)

###

@routes.route('/owasp/csrf_one/')
def owasp_csrf_one():
    if not "balance" in session.keys():
        session["balance"] = 100

    return render_template("owasp/csrf_one.html", balance=session["balance"])

@routes.route('/owasp/csrf_one_transfer/')
def owasp_csrf_one_transfer():
    amount = request.args.get('amount')
    session["balance"] -= int(amount)
    return redirect(url_for('routes.owasp_csrf_one'))

###

@routes.route('/owasp/csrf_two/')
def owasp_csrf_two():
    if not "balance" in session.keys():
        session["balance"] = 100

    return render_template("owasp/csrf_two.html", balance=session["balance"])

@routes.route('/owasp/csrf_two_transfer', methods=["POST"])
def owasp_csrf_two_transfer():
    amount = request.form.get('amount')
    session["balance"] -= int(amount)
    return redirect(url_for('routes.owasp_csrf_two'))

###

###########################
# TODO beyond this point
###########################

@routes.route('/owasp/csrf_three/')
def owasp_csrf_three():
    if not "balance" in session.keys():
        session["balance"] = 100

    return render_template("owasp/csrf_three.html", balance=session["balance"])

@routes.route('/owasp/csrf_three_transfer/')
def owasp_csrf_three_transfer():
    amount = request.form.get('amount')
    session["balance"] -= int(amount)
    return redirect(url_for('routes.owasp_csrf_three'))

###

@routes.route('/owasp/csrf_four/')
def owasp_csrf_four():
    if not "balance" in session.keys():
        session["balance"] = 100

    return render_template("owasp/csrf_four.html", balance=session["balance"])

@routes.route('/owasp/csrf_four_transfer/')
def owasp_csrf_four_transfer():
    amount = request.form.get('amount')
    session["balance"] -= int(amount)
    return redirect(url_for('routes.owasp_csrf_four'))

###

@routes.route('/owasp/csrf_five/')
def owasp_csrf_five():
    if not "balance" in session.keys():
        session["balance"] = 100

    return render_template("owasp/csrf_five.html", balance=session["balance"])

@routes.route('/owasp/csrf_five_transfer/')
def owasp_csrf_five_transfer():
    amount = request.form.get('amount')
    session["balance"] -= int(amount)
    return redirect(url_for('routes.owasp_csrf_five'))

##########################

@routes.route('/owasp/sqli/')
def owasp_sqli():
    return render_template("hello_html.html", name=request.args.get('name', '_name not specified_'))
