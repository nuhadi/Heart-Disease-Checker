from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=['POST'])
def analyze():
	# Berisi 13 attribute yang akan digunakan untuk kalkulasi
	attributes = request.data

	#
	# Kode utama disini
	#

	# Hasil akhir
	result = 4
	return jsonify(result)