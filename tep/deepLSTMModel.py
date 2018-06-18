import keras
from keras.models import Model
from keras.layers import Input, Dropout, Dense, Flatten
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.layers.normalization import BatchNormalization
from keras.layers.merge import concatenate

def classification_model(input_dim, output_dim, emb_mat, seq_len, lstm_layers=1, lstm_dim=32, ret_seq=True, fc_layers=1, fc_units=64, metrics=['acc']):
    """
    Compiles classification model which processes textual inputs using LSTM 
    layers and then merges them with (normalized) auxiliary inputs.
    """
    seqs = Input(shape=(seq_len,), dtype='int32', name='text_input')
    x = Embedding(emb_mat.shape[0], emb_mat.shape[1], weights=emb_mat, input_length=seq_len, trainable=True, name='word_embedding')(seqs)
    for i in range(1, lstm_layers + 1):
        lstm_name = 'lstm_' + str(i)
        x = LSTM(lstm_dim, return_sequences=ret_seq, name=lstm_name)
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

def regression_model(input_dim, emb_mat, seq_len, lstm_layers=1, lstm_dim=32, ret_seq=True, fc_layers=1, fc_units=64, metrics=['acc']):
    """
    Compiles regression model which processes textual inputs using LSTM 
    layers and then merges them with (normalized) auxiliary inputs.
    """
    seqs = Input(shape=(seq_len,), dtype='int32', name='text_input')
    x = Embedding(emb_mat.shape[0], emb_mat.shape[1], weights=emb_mat, input_length=seq_len, trainable=True, name='word_embedding')(seqs)
    for i in range(1, lstm_layers + 1):
        lstm_name = 'lstm_' + str(i)
        x = LSTM(lstm_dim, return_sequences=ret_seq, name=lstm_name)
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
