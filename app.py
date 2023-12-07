from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/products', "methods=['GET']")
def products():
    return render_template("products.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
