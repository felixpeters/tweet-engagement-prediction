import itertools
from itertools import chain
import keras
from keras.callbacks import ModelCheckpoint, History, EarlyStopping, TensorBoard, ReduceLROnPlateau
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
import keras.backend as K

def r2(y_true, y_pred):
    """
    Return r2 score as an additional metric for regression models.
    """
    SS_res =  K.sum(K.square(y_true-y_pred))
    SS_tot = K.sum(K.square(y_true - K.mean(y_true)))
    return (1 - SS_res/(SS_tot + K.epsilon()))

def get_callbacks(model_name, log_dir, stop_patience=10, lr_patience=5, verbose=0, emb_meta=None):
    """
    Return ModelCheckpoint, EarlyStopping and History callbacks as an array.
    """
    filename = "models/" + model_name + ".hdf5"
    checkpoint = ModelCheckpoint(filename, verbose=verbose, save_best_only=True, save_weights_only=True)
    early_stopping = EarlyStopping(patience=stop_patience, verbose=verbose)
    history = History()
    tensorboard = TensorBoard(log_dir=log_dir, histogram_freq=5, write_grads=True, embeddings_freq=0, embeddings_metadata=emb_meta)
    reduce_lr = ReduceLROnPlateau(factor=0.2, patience=lr_patience, verbose=verbose)
    return [checkpoint, early_stopping, history, tensorboard, reduce_lr]

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

def print_classification_metrics(history):
    """
    Print cross-entropy and accuracy metrics for training and validation set.
    """
    val_loss = history.history['val_loss']
    loss = history.history['loss']
    val_acc = history.history['val_acc']
    acc = history.history['acc']
    i = np.argmin(val_loss)
    print("loss: {}, acc: {}, val_loss: {}, val_acc: {}".format(loss[i], acc[i], val_loss[i], val_acc[i]))
    return

def print_regression_metrics(history):
    """
    Print MSE and R2 metrics for training and validation set.
    """
    val_loss = history.history['val_loss']
    loss = history.history['loss']
    val_r2 = history.history['val_r2']
    r2 = history.history['r2']
    i = np.argmin(val_loss)
    print("loss: {}, r2: {}, val_loss: {}, val_r2: {}".format(loss[i], r2[i], val_loss[i], val_r2[i]))
    return

def plot_cm(predictions, actuals, classes, normalize=False, cmap=plt.cm.Blues):
    """
    Create and plot confusion matrix for the given predictions.
    """
    cm = confusion_matrix(actuals, predictions) 
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        cm = cm.round(decimals=2)
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j], horizontalalignment="center", color="black")
    plt.tight_layout()
    plt.ylabel('Actual class')
    plt.xlabel('Predicted class')
    plt.show()
    return

def one_hot_encoding(class_labels, number_classes):
    """
    Returns one-hot encoded class labels.
    """
    labels = np.zeros((len(class_labels), number_classes))
    for index, class_label in enumerate(class_labels):
        labels[index, int(class_label)] = 1
    return labels

def one_hot_to_class(labels):
    """
    Undo one-hot encoding, i.e., return class number.
    """
    classes = np.empty(len(labels))
    for i, label in enumerate(labels):
        classes[i] = np.argmax(label)
    return classes
