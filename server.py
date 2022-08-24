from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("pizza_shop.html")

@app.route("/pepperoni")
def pepperoni():
    return render_template("pepperoni.html")

@app.route("/sausage")
def sausage():
    return render_template("sausage.html")

@app.route("/to-be-continued")
def final():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=True)