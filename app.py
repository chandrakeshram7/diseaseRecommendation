import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
class_indices = json.load(open("class_indices.json"))
# TensorFlow Serving endpoint URL
TF_SERVING_URL = 'http://tensorflow-serving-host:8501/v1/models/model_name:predict'

@app.route('/')
def home():
    return "Server is running"

@app.route('/predict')
def predict():
    # Assuming you have an image file path
    image_path = "healthy.webp"

    # Load and preprocess the image
    img_data = open(image_path, 'rb').read()

    # Prepare the JSON request payload
    payload = json.dumps({"instances": [{"b64": img_data}]})

    # Send prediction request to TensorFlow Serving
    response = requests.post(TF_SERVING_URL, data=payload)

    # Parse the prediction response
    predictions = json.loads(response.content)['predictions']
    predicted_class_index = predictions[0]['index']
    predicted_class_name = class_indices[str(predicted_class_index)]

    return jsonify({'Predicted_class': predicted_class_name})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
