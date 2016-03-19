from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

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

@app.route('/exfil/')
def hello_js():
    return render_template("exfil.html",
                           username=request.args.get('username', 'GrumpyCat'))

@app.route('/validate_email/')
def hello_js():
    return render_template("validate_email.html")

if __name__ == "__main__":
    app.run()
