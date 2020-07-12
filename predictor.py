import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.models import model_from_json

import os
import pickle
import math
import random
import csv
from PIL import Image

size = 32

pickle_file = './pre-data.pickle'
with open(pickle_file, 'rb') as f:
    pickle_data = pickle.load(f)
    signnames = pickle_data['signnames']

def preprocess_img(image):
    image = image.resize((size, size))
    image = np.array(image)
    image = image.reshape(1, size, size, 3)
    image = image.astype(np.float32) / 128.0 - 1.0
    return image

class Predictor: 
    def __init__(self):
        # load json and create model
        json_file = open('./model_a.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights("./model_a.h5")
        opt = keras.optimizers.Adam(learning_rate=0.0005)
        model.compile(loss="sparse_categorical_crossentropy",optimizer=opt,metrics=["accuracy"])
    
    def predict(self, request):
        '''
        This method reads the file uploaded from the Flask application POST request, 
        and performs a prediction using the loaded model. 
        '''
        # load json and create model
        json_file = open('./model_a.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights("./model_a.h5")
        opt = keras.optimizers.Adam(learning_rate=0.0005)
        model.compile(loss="sparse_categorical_crossentropy",optimizer=opt,metrics=["accuracy"])
        f = request.files['img1']
        src = Image.open(f)
        image = preprocess_img(src)
        pred = model.predict_classes(image)
        pred1 = signnames[int(pred[0])]
        prediction = "Traffic Sign Image is recognized as " + "class label: " + str(pred[0]) + " -- " + str(pred1)
        return prediction