import redis
from flask import Flask, request, jsonify

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    r.set('last_result', result)
    return jsonify({'result': result})

@app.route('/last')
def last():
    value = r.get('last_result')
    return jsonify({'last_result': value})
