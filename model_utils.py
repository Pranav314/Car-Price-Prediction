import pickle

def load_model():
    with open("car_price_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model
