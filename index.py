from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/analyze", methods=['POST'])
def analyze():
	attributes = request.data
    return str(5)