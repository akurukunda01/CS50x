from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/asian")
def asian():
    return render_template("asian.html")

@app.route("/indian")
def indian():
    return render_template("indian.html")

@app.route("/italian")
def italian():
    return render_template("italian.html")

@app.route("/middleeast")
def middleeast():
    return render_template("middleeast.html")

@app.route("/mexican")
def mexican():
    return render_template("mexican.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
