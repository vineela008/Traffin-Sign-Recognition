## [Data_preprocess.ipynb](https://github.com/vineela008/Traffin-Sign-Recognition/blob/master/Data_preprocess.ipynb)
Data loading from pickel datast and evaluation of data.

## [LeNet.ipynb](https://github.com/vineela008/Traffin-Sign-Recognition/blob/master/LeNet.ipynb)
Build, Train and Test the LeNet model.

### Layers of LeNet Model:
* Convolution
* Max pooling
* Convolution
* Max pooling
* Flatten
* 3 Fully connected

### Values of HyperParameters used to train the LeNet model:
* LEARNING_RATE = 1e-2  i.e; 0.01
* EPOCHS = 50
* BATCH_SIZE = 128

### Additional Methods used:
* ReLu (Rectified Linear Unit)
* Mini-batch gradient descent
* Dropout

## [AlexNet_DL.ipynb](https://github.com/vineela008/Traffin-Sign-Recognition/blob/master/AlexNet_DL.ipynb)
Build, Train and Test the AlexNet model.

### Layers of AlexNet Model:
* Convolution
* Max pooling
* Convolution
* Max pooling
* 3 Convolution
* Max pooling
* Flatten
* 3 Fully connected

### Values of HyperParameters used to train the AlexNet model:
* LEARNING_RATE = 5e-4
* EPOCHS = 30
* BATCH_SIZE = 128
* keep_prop = 0.5
* LAMBDA = 1e-5

### Additional Methods used:
* Adam optimization
* L2 regularization

## [GoogLeNet.ipynb](https://github.com/vineela008/Traffin-Sign-Recognition/blob/master/GoogLeNet.ipynb)
Build, Train and Test the GoogleNet model.

### Layers of GoogleNet Model:
* convolution
* 2 parallel inception layers
* max pooling
* 2 parallel inception layers
* max pooling
* 2 parallel inception layers
* avg pooling
* flatten
* Full connected

### Values of HyperParameters used to train the GoogleNet model:
* LEARNING_RATE = 5e-4
* EPOCHS = 25
* BATCH_SIZE = 128
* keep_prop = 0.5

### Additional Methods used:
* Inception Module
* Overlapping pooling


## Flask Application Demo
Run [app.py](https://github.com/vineela008/Traffin-Sign-Recognition/blob/master/app.py) for running application demo on localhost.

In this demo, user is asked to upload a traffic sign image, which is saved as input.png in [static](https://github.com/vineela008/Traffin-Sign-Recognition/tree/master/static) folder.

[predictor.py](https://github.com/vineela008/Traffin-Sign-Recognition/blob/master/predictor.py) is used to predict the class of user uploaded image using saved AlexNet model and displays classification results.

Corresponding html code is available in [templates](https://github.com/vineela008/Traffin-Sign-Recognition/tree/master/templates) folder.







