from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def actor():
    context = {
        # "caption": "Сайт фанатов Marvel",
        "link": "Посмотреть фильм",
    }
    return render_template("Dz_BooS.html", **context)
@app.route("/shablon/")
def actor2():
    context = {
        # "caption": "Актеры Marvel",
        "link": "Перейти на страничку актера"
    }
    return render_template("Dz_BooS.html", **context)

@app.route("/person/")
def films():
    return render_template("Dz_2.html")

@app.route("/contacts/")
def contacts():
    return render_template("Dz.html")

if __name__ == "__main__":
    app.run()