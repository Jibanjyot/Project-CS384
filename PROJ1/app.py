from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import os
import urllib.request
from proj1 import *

ALLOWED_EXTENSIONS = set(['csv'])

logging.basicConfig(level=logging.DEBUG)
UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app = Flask(__name__, static_url_path='')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
CORS(app)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/project', methods=['GET'])
def plotly():
    return app.send_static_file('index.html')

@app.route('/email', methods=['POST'])
def send_email():
    getMailData()
    resp = jsonify({'message' : 'No file part in the request'})
    resp.status_code = 200
    return resp	

@app.route('/concise', methods=['POST'])
def generate_concise():
    pmarks=int(request.form.get('pmarks'))
    nmarks=int(request.form.get('nmarks'))
    generateconciseMarksheets(pmarks,nmarks)
    resp = jsonify({'message' : 'Concise file is generated'})
    resp.status_code = 200
    return resp	

@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'masterFile' not in request.files or 'responseFile' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['masterFile']
	if file and allowed_file(file.filename):
		filename = 'master_roll.csv'
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	file = request.files['responseFile']
	if file and allowed_file(file.filename):
		filename = 'responses.csv'
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	pmarks=int(request.form.get('pmarks'))
	nmarks=int(request.form.get('nmarks'))
	print(pmarks,nmarks)
	generateMarksheets(pmarks,nmarks)
	resp = jsonify({'message' : 'Files generated succesfully'})
	resp.status_code = 200
	return resp
 	
if __name__ == "__main__":
    app.run(debug=True)
