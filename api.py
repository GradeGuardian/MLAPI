from flask import Flask
from flask import jsonify
from flask import request
import boto3
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=['POST'])
@cross_origin()
def predict():
        client = boto3.client('machinelearning')
        print(request.get_json())

        response = client.predict(
                MLModelId='ml-XjLZS3QPeBC',
                Record=request.get_json(),
                PredictEndpoint='https://realtime.machinelearning.us-east-1.amazonaws.com'
        )
        return jsonify(response)

@app.route("/test")
@cross_origin()
def hello():
        return 'Hello, World!'
