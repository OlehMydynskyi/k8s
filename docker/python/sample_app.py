from flask import Flask, redirect
from flask import request
from flask import render_template

sample = Flask(__name__)
@sample.route("/")
def main():
	return render_template("index.html", addr=request.remote_addr)

@sample.route("/cakes")
def test():
	return redirect("https://sentry.io/", code=302)

if __name__ == "__main__":
	sample.run(host="0.0.0.0", port=7070)
