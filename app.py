from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "iniSecretKeyKu2019"


@app.route("/")
def indexku():
    # belajar looping
    hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
    # conditioning / if-else
    suasana = "sedih"  # jika senang maka dia juga cinta jika tidak, maka dia sedih
    # set variabel
    return render_template("index.html", value=hari, suasana=suasana)


@app.route("/contact")
def contactku():
    return render_template("contact.html")


@app.route("/about")
def aboutku():
    return render_template("about.html")


# parsing nilai int, string
@app.route("/parsing/<string:nilaiku>")
def ayo_parsing(nilaiku):
    return "nilainya adalah : {}".format(nilaiku)


# argument parser
@app.route("/parsingargument")
def ayo_argument():
    data = request.args.get("nilai")
    return "nilainya dari argument parser adalah {}".format(data)


# memparsing nilai dari url untuk mengeset nilai session
@app.route("/halaman/<int:nilai>")
def session_1(nilai):
    session["nilaiku"] = nilai
    return "Berhasil mengeset nilainya"


@app.route("/halaman/lihat")
def view_session_1():
    try:  # try except ini sama dengan if else
        data = session["nilaiku"]
        return "Nilai yang telah diset adalah = {}".format(data)
    except:
        return "Anda tidak memiliki nilai session lagi"


# logout / destroy session
@app.route("/halaman/logout")
def logout_session_1():
    session.pop("nilaiku")
    return "Berhasil logout / menghapus session"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
