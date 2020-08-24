# AI

This repository is mostly based on Harvard's CS50 - AI (the master branch). All projects are completed by myself with some assistance from the ED forum. For a description of each project, you can visit the CS50-AI website in this link: https://cs50.harvard.edu/ai/2020/. Other branches contain some short assignments from CS50 itself for practice.


## PageRank:
Use Markov Chain and iterative algorithms to calculate page ranks - the importance of pages when searching

### Key Ideas:
- Markov Chain: a sequence of random variables where the distribution of each variable follows the Markov assumption
- Markov assumption: a current state depends on only a finite number of previous states
- Transition model: specify the probability distributions of the next event based on the values of the current event

## Heredity:
Use Bayesian network and inference by enumeration to find the heredity of impairment genes

### Key Ideas:
- Bayesian network: a directed graph data structure that represents the dependencies of random variables where an
arrow from one variable (X) to another variable (Y) is the conditional probability of Y based on X. Y is the parent of X.
- Inference by enumeration: a process of finding the probability distribution of variable X given some observed evidence
e and some hiddren variables Y.
- Joint probability: the liklihood of multiple events all occuring

## Crossword

### Optimization Concepts:
- Constraint Satisfaction Problem
- Backtracking Search
- Linear & nonlinear programming
- Hill climbing & simulated annealing

* Bonus review: Lagrange multipliers for solving constraint optimization

## Traffic: image classification
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
One of the key objectives of this project is to investigate the effects of tuning hyperparameters inside a convolutional neural network (CNN).

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

## Weather: random forest tutorial
Going to back environmental data, this time I'm learning to create an emsemble random forest classifier! The code is based on the tutorial from medium: https://towardsdatascience.com/random-forest-in-python-24d0893d51c0. 