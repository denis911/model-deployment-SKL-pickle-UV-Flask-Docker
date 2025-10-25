from flask import Flask
from flask import request
from flask import jsonify

app = Flask('Ping')

@app.route('/ping', methods=['GET'])
def ping():
    info = request.get_json()
    print('info received ', info)
    return jsonify(info)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
    # host='0.0.0.0' is localhost
    # http://127.0.0.1:9696/ping - open in a web browser
    # or curl http://127.0.0.1:9696/ping in a terminal
