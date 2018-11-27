#!/usr/bin/python

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from sklearn.externals import joblib

app = Flask(__name__)
CORS(app)



@app.route("/analyze", methods=['POST'])
def analyze():
	attributes = request.get_json()

	#
	mlp = joblib.load('model.mdl')
	result = mlp.predict([attributes])[0]
	#Kode utama disini
	#

	# Hasil akhir
	return jsonify(result)
	
