import keras
from keras.callbacks import ModelCheckpoint, History, EarlyStopping
import matplotlib.pyplot as plt

def get_callbacks(model_name, patience=5, verbose=0):
    """
    Return ModelCheckpoint, EarlyStopping and History callbacks as an array.
    """
    filename = "models/" + model_name + ".hdf5"
    checkpoint = ModelCheckpoint(filename, verbose=verbose, save_weights_only=True)
    early_stopping = EarlyStopping(patience=patience, verbose=verbose)
    history = History()
    return [checkpoint, early_stopping, history]

def plot_loss(history):
    """
    Plots training and validation loss over number of iterations.
    """
    x = range(1, len(history.epoch) + 1)
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    plt.plot(x, loss, 'r-', label='Training loss')
    plt.plot(x, val_loss, 'b-', label='Validation loss')
    plt.legend(loc='upper right')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.show()
    return
