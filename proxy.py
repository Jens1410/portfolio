from flask import Flask, Response, request
import requests

app = Flask(__name__)

TARGET = "http://127.0.0.1:8000"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    url = f"{TARGET}/{path}"

    # WICHTIG: Header für ngrok im REQUEST setzen
    outgoing_headers = dict(request.headers)
    outgoing_headers["ngrok-skip-browser-warning"] = "true"
    outgoing_headers["User-Agent"] = "Mozilla/5.0 (skip-ngrok-warning)"

    resp = requests.get(url, headers=outgoing_headers)

    # Response unverändert zurückgeben
    return Response(resp.content, resp.status_code, resp.headers.items())

if __name__ == "__main__":
    app.run(port=5000)