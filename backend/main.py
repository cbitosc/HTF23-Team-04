from flask import Flask, request, jsonify
from data_processing import get_data, choose_model
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type' #pip install -U flask-cors

@app.route('/')
def hello_world():
    return 'Hello, World!'


# http://127.0.0.1:5000/data_chart/IBM
@app.route('/data_chart/<string:symbol>')

# http://127.0.0.1:5000/data_chart/IBM/SMA
@app.route('/data_chart/<string:symbol>/<string:func>')
def data_chart(symbol, func=None):
    return jsonify(get_data(symbol, func))

# for model return
# @app.route('/model/<string:symbol>')
# def model(symbol):
#     result = call_model_function(choose_model(symbol))
#     # result of model should be in json format, (list of objects)

#     return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
