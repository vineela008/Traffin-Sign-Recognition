from flask import Flask, render_template, request, make_response
from functools import wraps, update_wrapper
from PIL import Image
from predictor import Predictor

import numpy as np
##import torch
import os

# Initialize the predictor object.
predictor = Predictor()

# Create constants for app root folder and image upload folder
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/upload", methods=['GET','POST'])
def upload():
    upl = request.files['img1']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'input.png')
    upl.save(filepath)
    prediction = predictor.predict(request)
    return render_template('predict.html', prediction=prediction)
        

if __name__ == '__main__':
    app.debug = True
    app.run(port = 5001)