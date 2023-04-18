from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.
@app.route('/process1', methods=['POST'])
def run_process1():
    data = request.get_json()
    theResult = process1(data)
    return jsonify(theResult)

@app.route('/process2', methods=['POST'])
def run_process2():
    data = request.get_json() 
    theResult = process2(data)
    return jsonify(theResult)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000 debug=True)
