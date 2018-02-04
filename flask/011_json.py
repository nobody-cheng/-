# coding:utf-8
from flask import Flask, request, abort, Response, make_response, jsonify
import json

app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
def index():
    data = {
        'name': 'xidada',
        'age': '22'
    }

    json_str = json.dumps(data)
    # return json_str, 200, {"Content-Type": "application/json"}
    # return jsonify(data)
    return jsonify(city="shenzhen", country="china")


if __name__ == '__main__':
    app.run(debug=True)
