from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def actor():
    context = {
        "link": "Перейти на страничку актера",
    }
    return render_template("about.html", active_page="actors", **context)

@app.route("/person/")
def films():
    context = {
        "link": "Посмотреть фильм"
    }
    return render_template("home.html", active_page="films", **context)

if __name__ == "__main__":
    app.run()