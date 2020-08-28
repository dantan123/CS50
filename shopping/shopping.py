import csv
import sys
# import datetime
# from time import strptime

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4

def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")
    
    #return load_data(sys.argv[1])

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")

def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence_list = []
    label_list = []
    first_row = True
    
    with open (filename, newline = '') as file:
        data = csv.reader(file, delimiter=' ')
        for row in data:
            # skip the first row only
            if first_row == True:
                first_row = False
                continue

            row_list = row[0].split(",")

            # format data types
            row_list[0] = int(row_list[0])
            row_list[1] = float(row_list[1])
            row_list[2] = int(row_list[2])
            row_list[3] = float(row_list[3])
            row_list[4] = int(row_list[4])
            for i in range(5,10):
                row_list[i] = float(row_list[i])
            for i in range(11, 15):
                row_list[i] = int(row_list[i])
            
            # citation: https://www.kite.com/python/answers/how-to-convert-between-month-name-and-month-number-in-python
            month_name = row_list[10]
            month_num = convert(month_name)
            if month_num != False:
                row_list[10] = int(month_num)
            else:
                raise ValueError

            row_list[15] = 1 if row_list[15] == 'Returning_Visitor' else 0
            for i in range(16, 18):
                row_list[i] = 1 if row_list[i] == 'TRUE' else 0
            
            label = row_list.pop()
            evidence = row_list
            evidence_list.append(evidence)
            label_list.append(label)
    
    # print(shopping_list)
    return (evidence_list, label_list)
    raise NotImplementedError

def convert (month_name):
    # notice that June is recorded as June instead of Jun
    month_num = {
        "Jan": 0,
        "Feb": 1,
        "Mar": 2,
        "Apr": 3,
        "May": 4,
        "June": 5,
        "Jul": 6,
        "Aug": 7,
        "Sep": 8,
        "Oct": 9,
        "Nov": 10,
        "Dec": 11
    }
    return month_num.get(month_name, False)

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neigh = KNeighborsClassifier(n_neighbors=1)
    model = neigh.fit(evidence,labels)
    return model
    raise NotImplementedError


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    total_pos_count = 0
    total_neg_count = 0
    true_pos_count = 0
    true_neg_count = 0

    for i in range(len(labels)):
        if labels[i] == 1:
            total_pos_count += 1
            if predictions[i] == 1:
                true_pos_count += 1
        else:
            total_neg_count += 1
            if predictions[i] == 0:
                true_neg_count += 1

    true_pos_rate = true_pos_count / total_pos_count
    true_neg_rate = true_neg_count / total_neg_count
    return(true_pos_rate, true_neg_rate)
    raise NotImplementedError


if __name__ == "__main__":
    main()
