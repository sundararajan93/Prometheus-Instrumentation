from flask import Flask, render_template, url_for, redirect, request
from prometheus_client import start_http_server, Counter

METRICS_PORT = 8080
REQUEST_COUNT = Counter('shop_request_count', 'Total HTTP requests count')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    REQUEST_COUNT.inc()
    return render_template("index.html")

@app.route('/products', methods=['GET'])
def products():
    REQUEST_COUNT.inc()
    return render_template("products.html")


if __name__ == "__main__":
    #To Start the metrics server
    start_http_server(METRICS_PORT)
    app.run(host="0.0.0.0", port=80, debug=True)
