# AI

This repository is based on Harvard's CS50 - AI (the master branch). All projects are completed by myself with some assistance from the ED forum. For a description of each project, you can visit the CS50-AI website in this link: https://cs50.harvard.edu/ai/2020/. Other branches contain some short assignments from CS50 itself for practice.

## Traffic
This is the project where I got to build a CNN for predicting German traffic signs and experiment with TensorFlow and OpenCV.

### Key Ideas: 
- multilayer neural network: artificial neural network with an input layer,
an output layer, and at least one hidden layer
- image convolution: applying a filter that adds each pixel value of an image
to its neighbours, weighted according to a kernel matrix
- pooling: reducing the size of an input by sampling from regions in the input
- max pooling: pooling by choosing the max value in each region
- dropout: temporaily removing units - selected at random - from a neural network
to prevent over-reliance on certain units

### Key Observations:
One of the key objectives of this project is to investigate the effects of varying
the parameters inside a convolutional neural network (CNN). 

In general, it can be observed that increasing the number of convolutional and pooling 
layers also increases the accuracy of the model. This is achieved by applying the 
convolutional and pooling twice. The first convolution and pooling allow lower-level
features to be extracted such as edges, curves, and shapes of the images. The second
time allows higher-level and more complex features to be extracted. 

Increasing the number of filters in the convolutional layer does not affect 
the overall accuracy of the model for a number of 10 epochs, even though the initial accuracies are low. Increasing the filter number or sizes increase the abstractions of the model. It can be reasoned that as the number of layers increases and as more higher-level features need to be extracted, increasing the filter number and sizes can increase the representational power of the layers. 

It can also be observed that increasing the number and sizes of hidden layers neither improve
nor worsen the accuracy of the model and the neural network. For other models however, this may affect the 
accuracy. On the other hand, while increasing the size of max pooling reduces the size of input, it comes at a significant drop of accuracy. 