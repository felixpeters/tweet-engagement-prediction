import keras
from keras.models import Model
from keras.layers import Input, Dropout, Dense
from keras.layers.convolutional import Conv1D, ZeroPadding1D
from keras.layers.pooling import MaxPooling1D
from keras.layers.embeddings import Embedding
from keras.layers.normalization import BatchNormalization
from keras.layers.merge import concatenate

def classification_model(input_dim, output_dim, emb_mat, seq_len, conv_layers=1, filters=32, filter_size=3, dropout=0.5, fc_layers=1, fc_units=64, metrics=['acc']):
    """
    Compiles classification model which processes textual inputs using convolutional
    layers and then merges them with (normalized) auxiliary inputs.
    """
    seqs = Input(shape=(seq_len,), dtype='int32', name='text_input')
    x = Embedding(emb_mat.shape[0], emb_mat.shape[1], weights=emb_mat, input_length=seq_len, trainable=True, name='word_embedding')(seqs)
    for i in range(1, conv_layers + 1):
        pad_name = 'pad_' + str(i)
        conv_name = 'conv_' + str(i)
        pool_name = 'pool_' + str(i)
        dropout_name = 'dropout_' + str(i)
        x = ZeroPadding1D(name=pad_name)(x)
        x = Conv1D(filters, filter_size, activation='relu', name=conv_name)(x)
        x = MaxPooling1D(name=pool_name)(x)
        x = Dropout(dropout, name=dropout_name)(x)
    flatten = Flatten(name='flatten')(x)
    aux_input = Input(shape=(input_dim,), name='aux_input')
    norm_inputs = BatchNormalization(name='bn_aux')(aux_input)
    x = concatenate([flatten, norm_inputs], name='comb_input')
    for i in range(1, fc_layers + 1):
        fc_name = 'fc_' + str(i)
        bn_name = 'bn_' + str(i)
        x = Dense(fc_units, activation='relu', name=fc_name)(x)
        x = BatchNormalization(name=bn_name)(x)
    output = Dense(output_dim, activation='softmax', name='output')(x)
    model = Model(inputs=[seqs, aux_input], outputs=[output])
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=metrics)
    return model

def regression_model(input_dim, emb_mat, seq_len, conv_layers=1, filters=32, filter_size=3, dropout=0.5, fc_layers=1, fc_units=64, metrics=['acc']):
    """
    Compiles classification model which processes textual inputs using convolutional
    layers and then merges them with (normalized) auxiliary inputs.
    """
    seqs = Input(shape=(seq_len,), dtype='int32', name='text_input')
    x = Embedding(emb_mat.shape[0], emb_mat.shape[1], weights=emb_mat, input_length=seq_len, trainable=True, name='word_embedding')(seqs)
    for i in range(1, conv_layers + 1):
        pad_name = 'pad_' + str(i)
        conv_name = 'conv_' + str(i)
        pool_name = 'pool_' + str(i)
        dropout_name = 'dropout_' + str(i)
        x = ZeroPadding1D(name=pad_name)(x)
        x = Conv1D(filters, filter_size, activation='relu', name=conv_name)(x)
        x = MaxPooling1D(name=pool_name)(x)
        x = Dropout(dropout, name=dropout_name)(x)
    flatten = Flatten(name='flatten')(x)
    aux_input = Input(shape=(input_dim,), name='aux_input')
    norm_inputs = BatchNormalization(name='bn_aux')(aux_input)
    x = concatenate([flatten, norm_inputs], name='comb_input')
    for i in range(1, fc_layers + 1):
        fc_name = 'fc_' + str(i)
        bn_name = 'bn_' + str(i)
        x = Dense(fc_units, activation='relu', name=fc_name)(x)
        x = BatchNormalization(name=bn_name)(x)
    output = Dense(1, activation='relu', name='output')(x)
    model = Model(inputs=[seqs, aux_input], outputs=[output])
    model.compile(optimizer='Adam', loss='mean_squared_error', metrics=metrics)
    return model
