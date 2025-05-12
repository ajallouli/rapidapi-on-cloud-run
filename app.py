import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/developper', methods=['GET'])
def get_developer():
    return jsonify({'dev': 'amine'})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'hello': 'ok'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
