import keras.backend as K
K.clear_session()

from tep.config import Config
config = Config()
classes = config.CLASSES
num_classes = len(classes) + 1
print("TASK SETUP")
print("Number of classes: {}".format(num_classes))

from tep.utils import load_array
seqs = load_array(filename="data/sequences_len48.bc")
emb_mat = load_array(filename="data/embedding_matrix_100dim.bc")
features = load_array(filename="data/auxiliary_features.bc")
labels = load_array(filename="data/classification_labels.bc")
print("Number of training examples: {}".format(features.shape[0]))
print("Sequence length: {}".format(seqs.shape[1]))
print("Number of words in embedding: {}".format(emb_mat.shape[0]))
print("Embedding dimension: {}".format(emb_mat.shape[1]))
print("Number of input features: {}".format(features.shape[1]))

from tep.trainUtils import one_hot_encoding
oh_labels = one_hot_encoding(class_labels=labels, number_classes=num_classes)

# define configurations to test
configs = [
        {'name': '1c32n_1fc64n_02d', 'conv_layers': 1, 'conv_filters': 32, 'fc_layers': 1, 'fc_units': 64, 'dropout': 0.2},
        {'name': '1c32n_1fc64n_05d', 'conv_layers': 1, 'conv_filters': 32, 'fc_layers': 1, 'fc_units': 64, 'dropout': 0.5},
        {'name': '1c32n_1fc128n_02d', 'conv_layers': 1, 'conv_filters': 32, 'fc_layers': 1, 'fc_units': 128, 'dropout': 0.2},
        {'name': '1c32n_1fc128n_05d', 'conv_layers': 1, 'conv_filters': 32, 'fc_layers': 1, 'fc_units': 128, 'dropout': 0.5},
        {'name': '1c32n_2fc64n_02d', 'conv_layers': 1, 'conv_filters': 32, 'fc_layers': 2, 'fc_units': 64, 'dropout': 0.2},
        {'name': '1c32n_2fc64n_05d', 'conv_layers': 1, 'conv_filters': 32, 'fc_layers': 2, 'fc_units': 64, 'dropout': 0.5},
        {'name': '1c32n_2fc128n_02d', 'conv_layers': 1, 'conv_filters': 32, 'fc_layers': 2, 'fc_units': 128, 'dropout': 0.2},
        {'name': '1c32n_2fc128n_05d', 'conv_layers': 1, 'conv_filters': 32, 'fc_layers': 2, 'fc_units': 128, 'dropout': 0.5},
        {'name': '1c64n_1fc64n_02d', 'conv_layers': 1, 'conv_filters': 64, 'fc_layers': 1, 'fc_units': 64, 'dropout': 0.2},
        {'name': '1c64n_1fc64n_05d', 'conv_layers': 1, 'conv_filters': 64, 'fc_layers': 1, 'fc_units': 64, 'dropout': 0.5},
        {'name': '1c64n_1fc128n_02d', 'conv_layers': 1, 'conv_filters': 64, 'fc_layers': 1, 'fc_units': 128, 'dropout': 0.2},
        {'name': '1c64n_1fc128n_05d', 'conv_layers': 1, 'conv_filters': 64, 'fc_layers': 1, 'fc_units': 128, 'dropout': 0.5},
        {'name': '1c64n_2fc64n_02d', 'conv_layers': 1, 'conv_filters': 64, 'fc_layers': 2, 'fc_units': 64, 'dropout': 0.2},
        {'name': '1c64n_2fc64n_05d', 'conv_layers': 1, 'conv_filters': 64, 'fc_layers': 2, 'fc_units': 64, 'dropout': 0.5},
        {'name': '1c64n_2fc128n_02d', 'conv_layers': 1, 'conv_filters': 64, 'fc_layers': 2, 'fc_units': 128, 'dropout': 0.2},
        {'name': '1c64n_2fc128n_05d', 'conv_layers': 1, 'conv_filters': 64, 'fc_layers': 2, 'fc_units': 128, 'dropout': 0.5},
]

print("Testing a total of {} network architectures".format(len(configs)))
print("\n")

# Train model

# use settings for testing on sample
train_size = 1000
val_size = 100
batch_size = 64

# use settings for running on full data
#val_size = 10000
#train_size = features.shape[0] - val_size
#batch_size = 512

root_name = 'dmin_class'
root_path = 'models/' + root_name

from tep.deepConvModel import classification_model
from tep.modelUtils import save_architecture
from tep.trainUtils import get_callbacks, print_classification_metrics

print("START MODEL TRAINING")
print("\n")

for config in configs[:2]:
    # clear tf session first in order to avoid conflicts
    K.clear_session()

    # set model path
    model_name = root_name + '_' + config['name']
    model_path = root_path + '_' + config['name']
    logging_path = root_path + '/' + config['name']
    
    # Start logging
    print("Start training model: " + model_name)
    print("Training set: {} examples".format(train_size))
    print("Validation set: {} examples".format(val_size))
    
    # Create logging directory
    get_ipython().system('mkdir -p $logging_path')
    # Remove prior logs
    get_ipython().system('rm $logging_path/*')

    model = classification_model(
            features.shape[1],
            num_classes,
            emb_mat,
            seqs.shape[1],
            conv_layers=config['conv_layers'],
            filters=config['conv_filters'],
            dropout=config['dropout'],
            fc_layers=config['fc_layers'],
            fc_units=config['fc_units'],
    )
    save_architecture(model, model_path + '.json')

    # load model callbacks
    cbs = get_callbacks(model_name=model_name, log_dir=logging_path, verbose=1, emb_freq=5)

    # train model
    model.fit(
            {'text_input': seqs[:train_size], 'aux_input': features[:train_size]},
            {'output': oh_labels[:train_size]},
            validation_data=({'text_input': seqs[-val_size:], 'aux_input': features[-val_size:]}, {'output': oh_labels[-val_size:]}),
            batch_size=batch_size,
            epochs=200,
            verbose=0,
            shuffle=True,
            callbacks=cbs,
    )

    # print best result
    history = cbs[2]
    print_classification_metrics(history)
    print('\n')

print("END MODEL TRAINING")
