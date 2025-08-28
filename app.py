from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/new")
def new():
    return render_template("new_feature.html")

if __name__ == "__main__":
    app.run(debug=True)
