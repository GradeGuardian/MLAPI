from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
import boto3
@app.route("/", methods=['POST'])
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
def hello():
        return 'Hello, World!'
