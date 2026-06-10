import pandas as pd

def preprocess_data(df):
    """
    Split features and target.
    """

    X = df.drop('CLass', axis=1)
    y = df["Class"]

    return X, y