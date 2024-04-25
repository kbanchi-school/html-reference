from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/sora")
def index():
    return render_template("sora.html")

app.run()