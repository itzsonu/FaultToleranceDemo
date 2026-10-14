from flask import Flask, jsonify
import requests
from threading import Lock
 
app = Flask(__name__)
BACKENDS = [
    'http://127.0.0.1:5003',
    'http://127.0.0.1:5004',
    'http://127.0.0.1:5005'
]
index = 0
lock = Lock()
 
@app.get('/library')
def forward_request():
    global index
    with lock:
        start = index
        index = (index + 1) % len(BACKENDS)
 
    attempted = []
    for offset in range(len(BACKENDS)):
        backend = BACKENDS[(start + offset) % len(BACKENDS)]
        attempted.append(backend)
        try:
            response = requests.get(backend + '/library',
                                    timeout=1)
            response.raise_for_status()
            result = response.json()
            result['attempted_backends'] = attempted
            return jsonify(result), 200
        except (requests.exceptions.RequestException, ValueError):
            continue
 
    return jsonify({
        'error': 'No Library Service instance available',
        'attempted_backends': attempted
    }), 503
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000,
            debug=False, threaded=True)
