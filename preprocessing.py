import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    df = df.copy()
    
    # Drop ID
    df.drop("CustomerID", axis=1, inplace=True)
    
    # Encode categorical variables
    cat_cols = df.select_dtypes(include='object').columns
    
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])
    
    return df