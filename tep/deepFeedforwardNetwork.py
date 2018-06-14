import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam

def classification_model(input_dim, output_dim, num_layers, num_units, metrics=['acc']):
    """
    Compiles classification model with the given number of hidden layers and
    units. Inputs and all weights are normalized using BatchNorm.
    """
    model = Sequential()
    model.add(BatchNormalization(input_shape=(input_dim,), name='normalized_inputs'))
    for i in range(1, num_layers + 1):
        name = 'fc_' + str(i)
        bn_name = 'bn_' + str(i)
        model.add(Dense(num_units, activation='relu', name=name))
        model.add(BatchNormalization(name=bn_name))
    model.add(Dense(output_dim, activation='softmax', name='output'))
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=metrics)
    return model

def regression_model(input_dim, num_layers, num_units, metrics=[]):
    """
    Compiles regression model with the given number of hidden layers and
    units. Inputs and all weights are normalized using BatchNorm.
    """
    model = Sequential()
    model.add(BatchNormalization(input_shape=(input_dim,), name='normalized_inputs'))
    for i in range(1, num_layers + 1):
        name = 'fc_' + str(i)
        bn_name = 'bn_' + str(i)
        model.add(Dense(num_units, activation='relu', name=name))
        model.add(BatchNormalization(name=bn_name))
    model.add(Dense(1, activation='relu', name='output'))
    model.compile(optimizer='Adam', loss='mean_squared_error', metrics=metrics)
    return model
