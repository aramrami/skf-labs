import os
from flask import Flask, request, url_for, render_template, redirect


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")


@app.route("/home", methods=['POST'])
def home():
    sizeImg = request.form['size']
    os.system('convert static/img/bones.png -resize '+sizeImg+'% static/img/bones.png')
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
	


