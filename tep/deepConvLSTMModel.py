import keras
from keras.models import Model
from keras.layers import Input, Dropout, Dense, Flatten
from keras.layers.convolutional import Conv1D, ZeroPadding1D
from keras.layers.recurrent import LSTM
from keras.layers.pooling import MaxPooling1D
from keras.layers.embeddings import Embedding
from keras.layers.normalization import BatchNormalization
from keras.layers.merge import concatenate

def regression_model(input_dim, emb_mat, seq_len, conv_layers=1, conv_filters=32, filter_size=3, lstm_dim=32, fc_layers=1, fc_units=64, dropout=0.0, metrics=[]):
    """
    Compiles a model that learns representations from convolutional and
    recurrent layers. These representations are combined with auxiliary input,
    informing about the tweet context.
    """
    seqs = Input(shape=(seq_len,), dtype='int32', name='text_input')
    emb = Embedding(emb_mat.shape[0], emb_mat.shape[1], weights=[emb_mat], input_length=seq_len, trainable=True, name='word_embedding')(seqs)
    lstm = LSTM(lstm_dim, name='lstm_1')(emb)
    x = ZeroPadding1D(name='pad_1')(emb)
    x = Conv1D(conv_filters, filter_size, activation='relu', name='conv_1')(x)
    x = MaxPooling1D(name='pool_1')(x)
    for i in range(2, conv_layers + 1):
        pad_name = 'pad_' + str(i)
        conv_name = 'conv_' + str(i)
        pool_name = 'pool_' + str(i)
        x = ZeroPadding1D(name=pad_name)(x)
        x = Conv1D(conv_filters, filter_size, activation='relu', name=conv_name)(x)
        x = MaxPooling1D(name=pool_name)(x)
    flatten = Flatten(name='flatten')(x)
    aux_input = Input(shape=(input_dim,), name='aux_input')
    norm_inputs = BatchNormalization(name='bn_aux')(aux_input)
    x = concatenate([flatten, lstm, norm_inputs], name='comb_input')
    x = Dropout(dropout, name='dropout_1')(x)
    for i in range(1, fc_layers + 1):
        fc_name = 'fc_' + str(i)
        bn_name = 'bn_' + str(i)
        x = Dense(fc_units, activation='relu', name=fc_name)(x)
        x = BatchNormalization(name=bn_name)(x)
    output = Dense(1, activation='relu', name='output')(x)
    model = Model(inputs=[seqs, aux_input], outputs=[output])
    model.compile(optimizer='Adam', loss='mean_squared_error', metrics=metrics)
    return model
