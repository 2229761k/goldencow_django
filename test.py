from flask import Flask, request, jsonify

import json
import requests

app = Flask(__name__)

@app.route('/testing/', methods=['GET', 'POST'])
def testing():
    content = request.json
    symbol = content['symbol']
    print(symbol)

    return jsonify({'result' : 'success'})



if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=False)