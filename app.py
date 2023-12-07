from flask import Flask, render_template, url_for, redirect, request
from prometheus_client import Counter, start_http_server

app = Flask(__name__)
METRICS_PORT = 8080
REQUEST_COUNT = Counter('shop_request_count', 'Total HTTP requests count', ['application', 'route'])


@app.route('/', methods=['GET'])
def index():
    path = request.path
    REQUEST_COUNT.labels(application='shop',route=path).inc()
    return render_template("index.html")

@app.route('/products', methods=['GET'])
def products():
    path = request.path
    REQUEST_COUNT.labels(application='shop',route=path).inc()
    return render_template("products.html")

if __name__ == "__main__":
    #To Start the metrics server
    start_http_server(METRICS_PORT)
    app.run(host="0.0.0.0", port=80, debug=False)