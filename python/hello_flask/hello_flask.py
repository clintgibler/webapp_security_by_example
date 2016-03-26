from flask import Flask
from flask import render_template
from flask import request, session

app = Flask(__name__)

# Routes

@app.route("/")
def index():
    return render_template("index.html")
2
@app.route('/hello_html/')
def hello_html():
    return render_template("hello_html.html", name=request.args.get('name', ''))

@app.route('/hello_html_attr/')
def hello_html_attr():
    return render_template("hello_html_attr.html",
                           style=request.args.get('style', 'color:blue'))

@app.route('/hello_js/')
def hello_js():
    return render_template("hello_js.html",
                           username=request.args.get('username', 'GrumpyCat'))

# --- 
@app.route('/validate_email/')
def hello_validate_email():
    return render_template("validate_email.html")

# In progress
# @app.route('/hello_dropdown/')
# def hello_dropdown():
#     return render_template("hello_dropdown.html")

@app.route('/exfil/')
def hello_exfil():
    session['user_email'] = "joebob@somewhere.com"
    return render_template("exfil.html",
                           username=request.args.get('username', '[enter user name]'))


# Server config

app.secret_key = '0mG_So#S3kreT-4nd_unGuEss4ble'

app.config.update(
    SESSION_COOKIE_HTTPONLY = False
)

if __name__ == "__main__":
    app.run()
