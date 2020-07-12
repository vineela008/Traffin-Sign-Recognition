# Traffin-Sign-Recognition
As part of this project work, I tried three different Convolutional Neural Network architectures named LeNet, AlexNet and GoogleNet to classify Traffic Signs.

## Dataset
I used the [German Traffic Sign Recognition Benchmark]( http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset) Dataset for training and validating the models.

Download the data set [here]( https://d17h27t6h515a5.cloudfront.net/topher/2017/February/5898cd6f_traffic-signs-data/traffic-signs-data.zip). This is a pickled dataset in which the images are already resized to 32x32. It contains a training, validation and test set.

## Steps of the project
1. Data loading and pre-processing
2.  Building three models LeNet, AlexNet and GoogleNet
3. Training and evaluating the models using GTSRB dataset
4. Testing the models for unknown images from the web
5. Flask application demo for classiying user input Traffic sign images.

## Results
Training, validation and testing accuracies of three models are given below:

### LeNet
![net1](https://github.com/vineela008/Traffin-Sign-Recognition/blob/master/test_images/net1.JPG)

### AlexNet
![net2](https://github.com/vineela008/Traffin-Sign-Recognition/blob/master/test_images/net2.JPG)

### GoogleNet
![net3](https://github.com/vineela008/Traffin-Sign-Recognition/blob/master/test_images/net3.JPG)
