import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

features = pd.read_csv('temps.csv')
features.head(5)

print("The shapes of our features is: ", features.shape)

# show the statistics
features.describe()

# turn days of the week into binary using one-hot encoding
features = pd.get_dummies(features)

# show the first five row and last thirteen columns
features.iloc[0:5, 5:]

# labels are the values for predicting
# only extract the 'actual' column
labels = np.array(features['actual'])

# remove those labels from features, axis 1 referring to columns
features = features.drop('actual', axis = 1)

# save those features for later use
feature_list = list(features.columns)

# convert to numpy arrays
features = np.array(features)

# split data into test and training
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.25, random_state=42)
#print("Train features shape :", train_features.shape)
#print("Test features shape :", test_features.shape)
#print("Train labels shape", train_labels.shape)
#print("Test labels shape", test_labels.shape)
#print('test labels are :', test_labels)

# set baseline predictions as historical averages
# all rows and only the average column
baseline_preds = test_features[:, feature_list.index('average')]
#print("baseline predictions are : ", baseline_preds)

# set baseline errors to be the mean difference between the baseline preds and the test labels
baseline_errors = abs(baseline_preds - test_labels)
print("average baseline error: ", round(np.mean(baseline_errors)), "degrees.")

# train
# instantiate model with 1000 decision trees  with feature randomness
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)

# train the model on training data
rf.fit(train_features, train_labels)

# now make predictions on the test data
predictions = rf.predict(test_features)

# calculate the abs error
errors = abs(predictions - test_labels)
print("mean absolute error: ", round(np.mean(errors), 2), "degrees.")

# performance
# calculate mape
mape = 100 * (errors / test_labels)

# calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('accuracy:', round(accuracy, 2), '%.')