# Traffic

Create a convolutional neural network (CNN) for AI to predict traffic signs. 

Experimentation process:
One of the key objectives of this project is tuning the hyperparameters of a convolutional neural network (CNN).

In general, it can be observed that increasing the number of convolutional and pooling 
layers also increases the accuracy of the model. This is achieved by applying the 
convolutional and pooling twice. The second time allows higher-level and more complex features to be extracted. 

Increasing the number of filters in the convolutional layer does not affect 
the overall accuracy of the model for a number of 10 epochs, even though the initial accuracies are low. Increasing the filter number or sizes increase the abstractions of the model. It can be reasoned that as the number of layers increases and as more higher-level features need to be extracted, increasing the filter number and sizes can increase the representational power of the layers. 

It can also be observed that increasing the number and sizes of hidden layers neither improve
nor worsen the accuracy of the model and the neural network. For other models however, this may affect the 
accuracy. On the other hand, while increasing the size of max pooling reduces the size of input, it comes at a significant drop of accuracy.

Data can be found at https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip

