import pickle
import numpy as np

# Load model
model = pickle.load(open("../model.pkl", "rb"))

def predict(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction