import keras.backend as K
from keras.callbacks import ModelCheckpoint, History, TensorBoard
from tep.modelUtils import load_architecture
from tep.utils import load_array
K.clear_session()

# load the data and embedding weights
inputs = load_array('data/lang_model/inputs.bc')
labels = load_array('data/lang_model/labels.bc')
emb_mat = load_array('data/lang_model/emb_mat.bc')

print('Number of training examples: {}'.format(inputs.shape[0]))
print('Sequence length: {}'.format(inputs.shape[1]))
print('Number of words in embedding: {}'.format(emb_mat.shape[0]))
print('Embedding dimension: {}'.format(emb_mat.shape[1]))

# define configurations to test
configs = ['baseline_lstm', 
        'standard_lstm', 
        'standard_lstm_wd', 
        'standard_lstm_dropout', 
        'variational_lstm_dropout']

print("Testing a total of {} network architectures".format(len(configs)))

# configure logging
root_path = 'models/lang_model/'
log_path = 'models/lang_model/train/'

for config in configs:
    # clear TF session first in order to avoid conflicts
    K.clear_session()

    # set logging path
    model_file = root_path + config + '.json'
    weights_file = root_path + config + '.hdf5'
    logging_dir = log_path + config
    get_ipython().system('mkdir -p $logging_dir')
    get_ipython().system('rm $logging_dir/*')
    get_ipython().system('cp data/lang_model/word_labels.tsv $logging_dir')

    # load and compile model
    model = load_architecture(model_file)
    model.load_weights(weights_file)
    model.compile(loss='categorical_crossentropy', 
            optimizer='adam', 
            metrics=['accuracy'])
    
    # define training callbacks
    history = History()
    tensorboard = TensorBoard(log_dir=logging_dir)
    checkpoint = ModelCheckpoint(weights_file, verbose=1, save_best_only=True, save_weights_only=True)
    cbs = [history, tensorboard, checkpoint]

    model.fit(inputs, labels, batch_size=64, epochs=3, verbose=1, callbacks=cbs)

print('END MODEL TRAINING')


