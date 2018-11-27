from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/analyze", methods=['POST'])
def analyze():
	attributes = request.data
	return jsonify(5)