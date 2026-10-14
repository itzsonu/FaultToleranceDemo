from flask import Flask, jsonify
import sys
 
app = Flask(__name__)
port = int(sys.argv[1])
 
@app.get('/library')
def library():
    return jsonify({
        'message': 'Library request processed',
        'instance_port': port
    })
 
@app.get('/health')
def health():
    return jsonify({'status': 'healthy', 'port': port})
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=port,
            debug=False, threaded=True)
