# Hello Flask

Here are some simple examples of cross-site scripting (XSS) and client-side security using the Flask framework.

They are purposefully minimal examples so the underlying principle is clear, and not obscured by the complexity of a semi-real web app.

## Setup

Install Flask and other dependencies. For the following steps:
* If you're going to use Python 2, use `python` and `pip`
* If you're going to use Python 3, use `python3` and `pip3`

These examples were written using Python 3 but should work fine with Python 2.

```bash
# 1. Install dependencies
# Pass in --user to install dependencies just for this user rather
#   than system-level
$ pip install -r requirements.txt --user

# 2. Run the server
# Note that due to relative pathing this command should be run
# from within this current hello_flask/ directory
$ python hello_flask.py
```

Then navigate in your browser to `http://localhost:5000`.
