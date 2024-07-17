from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def actor():
    return render_template("Dz_BooS.html")  # Внутри () пишем название html-файла в кавычках
@app.route("/person/")
def films():
    return render_template("Dz_2.html")

@app.route("/contacts/")
def contacts():
    return render_template("Dz.html")

if __name__ == "__main__":
    app.run()