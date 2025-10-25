from flask import Flask
from flask import request
from flask import jsonify

app = Flask('Ping')

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    msg = request.args.get('msg', default='PONG') # .get_json() # if I need to receive json requests like an API
    print('info received: ', msg)
    return jsonify(message=msg)    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
    # host='0.0.0.0' is localhost
    # http://127.0.0.1:9696/ping - open in a web browser
    # http://127.0.0.1:9696/ping?msg=hello - with custom messages
    # http://127.0.0.1:9696/ping?msg=long%20way%20to%20knowledge - message with spaces
    # or curl http://127.0.0.1:9696/ping in a terminal
