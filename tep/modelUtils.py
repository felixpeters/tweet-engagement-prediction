import json
import keras
from keras.models import model_from_json

def save_architecture(model, filename):
    """
    Creates model config as json and saves to given file.
    """
    config = model.to_json()
    with open(filename, 'w') as f:
        json.dump(config, f, sort_keys=True)
        f.write("\n")
    return

def load_architecture(filename):
    """
    Creates model from config in the given file.
    """
    config = {}
    with open(filename) as f:
        for line in f:
            config = json.loads(line)
    model = model_from_json(config)
    return model
