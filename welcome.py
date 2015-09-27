import os
from flask import Flask
from flask import request
from flask import render_template
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/sha256')
def sha256():
    return render_template("sha256.html")

@app.route('/sha256', methods=['POST'])
def sha256_post():
    text = request.form['text']
    sha2 = hashlib.sha256(text)
    hex_dig = sha2.hexdigest().upper()
    return render_template("sha256.html", in1 = text, out1 = hex_dig)

port = os.getenv('VCAP_APP_PORT', '5000')

if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0', port=int(port))