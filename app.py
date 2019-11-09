from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "iniSecretKeyKu2019"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/redirect-about")
def ayo_redirect_about():
    return redirect(url_for("about"))


@app.route("/redirect-contact")
def ayo_redirect_contact():
    return redirect(url_for("contact"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
