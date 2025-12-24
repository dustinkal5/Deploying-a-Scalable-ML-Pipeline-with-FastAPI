import pytest
import pandas as pd
import numpy as np
import os
from ml import data, model
from sklearn.linear_model import LogisticRegression
from ml.model import train_model
# TODO: add necessary import

#loading csv for testing
def test_path():
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)
    return data



# TODO: implement the first test. Change the function name and input as needed
def test_cols():
    
    # Your code here
    assert test_path().shape[1]==15
    """
    # ensuring there are 15 cols in the dataset
    """

    pass


# TODO: implement the second test. Change the function name and input as needed
def test_size():

    assert test_path().shape[0]>5000

    """
    # ensuring the model has enough data to be trained on
    """
    pass
    

# TODO: implement the third test. Change the function name and input as needed
def test_model_uses_logistic_regression():
    X = np.array([[0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1])

    model = train_model(X, y)

    assert isinstance(model, LogisticRegression)
    """
    # ensuring the model being used is a Logistic Regression
    """
   
    # Your code here
    pass
