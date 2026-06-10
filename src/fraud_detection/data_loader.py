import pandas as pd



def load_data(filepath):
    """
    Load fraud detection dataset.
    """
    df = pd.read_csv(filepath)
    return df


if __name__ == "__main__":
    df = load_data("data/creditcard.csv")
print(df.head())
print("\nShape:", df.shape)