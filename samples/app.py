from flask import Flask, jsonify, request
import function
app = Flask(__name__)
@app.route('/get_catalan_nos/', methods=['GET', 'POST'])
def welcome():
    for i in range(50):
        value = function.catalan(i)
        print("Value is:-", value)
    return jsonify({"result": value})

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')