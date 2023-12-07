import time
from flask import Flask, render_template, url_for, redirect, request
from prometheus_client import Counter, start_http_server, Gauge


app = Flask(__name__)
METRICS_PORT = 8080
# Metrics Counters and Gauges
REQUEST_COUNT = Counter('shop_request_count', 'Total HTTP requests count', ['application', 'route'])
REQUEST_IN_PROGRESS = Gauge('shop_requests_pending', 'HTTP requests in Pending state', ['application', 'route'])
REQUEST_LAST_SERVED = Gauge('shop_requests_last_served', 'HTTP requests last served', ['application', 'route'])
REQUEST_BY_IP = Counter("shop_requests_by_ipAddr", "Total HTTP reqests based on IP address", ['application', 'route', 'ip_address'])

@app.route('/', methods=['GET'])
def index():
    path = request.path
    src_ip = request.remote_addr
    REQUEST_IN_PROGRESS.labels(application='shop',route=path).inc()
    REQUEST_BY_IP.labels(application='shop',route=path, ip_address=src_ip).inc()
    REQUEST_COUNT.labels(application='shop',route=path).inc()
    time.sleep(5)
    REQUEST_LAST_SERVED.labels(application='shop',route=path).set(time.time())
    REQUEST_IN_PROGRESS.labels(application='shop',route=path).dec()
    return render_template("index.html")

@app.route('/products', methods=['GET'])
def products():
    path = request.path
    src_ip = request.remote_addr
    REQUEST_IN_PROGRESS.labels(application='shop',route=path).inc()
    REQUEST_BY_IP.labels(application='shop',route=path, ip_address=src_ip).inc()
    time.sleep(5)
    REQUEST_LAST_SERVED.labels(application='shop',route=path).set(time.time())
    REQUEST_IN_PROGRESS.labels(application='shop',route=path).dec()
    return render_template("products.html")

if __name__ == "__main__":
    #To Start the metrics server
    start_http_server(METRICS_PORT)
    app.run(host="0.0.0.0", port=80, debug=False)