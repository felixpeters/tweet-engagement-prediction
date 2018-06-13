import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam

def classification_model(input_dim, output_dim, opt=Adam(), metrics=['acc']):
    """
    Generates compiled classification model, inputs are normalized using BatchNorm.
    """
    model = Sequential([
        BatchNormalization(input_shape=(input_dim,), name='normalized_inputs'),
        Dense(output_dim, activation='softmax', name='output')
    ])
    model.compile(opt, loss='categorical_crossentropy', metrics=metrics)
    return model

def regression_model(input_dim, opt=Adam(), metrics=[]):
    """
    Generates compiled regression model, inputs are normalized using BatchNorm.
    Output activation is ReLU since negative numbers do not make sense in
    this setting.
    """
    model = Sequential([
        BatchNormalization(input_shape=(input_dim,)),
        Dense(1, activation='relu')
    ])
    model.compile(opt, loss='mean_squared_error', metrics=metrics)
    return model
