# Hello Flask

Here are some simple examples of cross-site scripting (XSS) and client-side security using the Flask framework.

They are purposefully minimal examples so the underlying principle is clear, and not obscured by the complexity of a semi-real web app.

## Setup

Install Flask and other dependencies. For the following steps:
* If you're going to use Python 2, use `python` and `pip`
* If you're going to use Python 3, use `python3` and `pip3`

These examples were written using Python 3 but should work fine with Python 2.

```bash
# 1. Clone this repo, that's better than downloading the source code because
# it'll be easier to get updates.
$ git clone https://github.com/clintgibler/webapp_security_by_example.git

# 2. Install dependencies
# Pass in --user to install dependencies just for this user rather
#   than system-level
$ pip install -r requirements.txt --user

# 3. Run the server
# Note that due to relative pathing this command should be run
# from within this current hello_flask/ directory
$ python hello_flask.py
```

Then navigate in your browser to `http://localhost:5000`.

## Running with Vagrant

If you're running `hello_flask.py` in a Vagrant VM you may find that when you
try to load `http://localhost:5000` in a browser on your *host* that you can't see
the web app.

This is because by default Flask runs apps on `localhost` only, so we need to tell
it to be accessible from your host. Change `hello_flask.py` to

    app.run(host='0.0.0.0')

**Note**: This is making Flask visible on the network, which is useful for
accessing it from your host machine but potentially dangerous, as this web app
is intentionally vulnerable, allowing a malicious user to run shell commands
or read files from your computer.

See [these](http://stackoverflow.com/questions/31904761/what-does-app-runhost-0-0-0-0-mean-in-flask) [Stack Overflow](http://stackoverflow.com/questions/7023052/flask-configure-dev-server-to-be-visible-across-the-network) threads for more details.

If your machine has a public IP address (e.g. is accessible over the Internet, not
just your local machine), it'd probably be safer to run this on your host OS and
bind it only to `localhost`, as it's currently configured.
