from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=['POST'])
def analyze():
	attributes = request.data
	return jsonify(5)