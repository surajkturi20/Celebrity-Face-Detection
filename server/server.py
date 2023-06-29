
from flask_cors import CORS  # Import CORS from flask_cors
from flask import Flask, request, jsonify
import util


# CORS policy error resolved
app = Flask(__name__)
CORS(app)  # Add CORS middleware to your Flask app


app = Flask(__name__)



@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))


    response.headers.add('Access-Control-Allow-Origin', '*')

    # new lines
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)