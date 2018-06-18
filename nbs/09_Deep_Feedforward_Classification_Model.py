import keras.backend as K
K.clear_session()

from tep.config import Config
config = Config()
classes = config.CLASSES
num_classes = len(classes) + 1
print("TASK SETUP")
print("Number of classes: {}".format(num_classes))

from tep.utils import load_array
features = load_array(filename="data/auxiliary_features.bc")
labels = load_array(filename="data/classification_labels.bc")
print("Number of training examples: {}".format(features.shape[0]))
print("Number of input features: {}".format(features.shape[1]))
print("\n")

from tep.trainUtils import one_hot_encoding
oh_labels = one_hot_encoding(class_labels=labels, number_classes=num_classes)

# define configurations to test
configs = [
    {'name': '1h_16n', 'num_layers': 1, 'num_units': 16},
    {'name': '1h_32n', 'num_layers': 1, 'num_units': 32},
    {'name': '1h_64n', 'num_layers': 1, 'num_units': 64},
    {'name': '2h_16n', 'num_layers': 2, 'num_units': 16},
    {'name': '2h_32n', 'num_layers': 2, 'num_units': 32},
    {'name': '2h_64n', 'num_layers': 2, 'num_units': 64},
    {'name': '3h_16n', 'num_layers': 3, 'num_units': 16},
    {'name': '3h_32n', 'num_layers': 3, 'num_units': 32},
    {'name': '3h_64n', 'num_layers': 3, 'num_units': 64},
    {'name': '4h_16n', 'num_layers': 4, 'num_units': 16},
    {'name': '4h_32n', 'num_layers': 4, 'num_units': 32},
    {'name': '4h_64n', 'num_layers': 4, 'num_units': 64},
    {'name': '5h_16n', 'num_layers': 5, 'num_units': 16},
    {'name': '5h_32n', 'num_layers': 5, 'num_units': 32},
    {'name': '5h_64n', 'num_layers': 5, 'num_units': 64},
]

print("Testing a total of {} network architectures".format(len(configs)))

# Train model

# use settings for testing on sample
#train_size = 10000
#val_size = 1000
#batch_size = 64

# use settings for running on full data
val_size = 10000
train_size = features.shape[0] - val_size
batch_size = 512

root_name = 'dffn_class'
root_path = 'models/' + root_name

from tep.deepFeedforwardNetwork import classification_model
from tep.modelUtils import save_architecture
from tep.trainUtils import get_callbacks, print_classification_metrics

print("START MODEL TRAINING")
print("\n")

for config in configs:
    # clear tf session first in order to avoid conflicts
    K.clear_session()

    # set model path
    model_name = root_name + '_' + config['name']
    model_path = root_path + '_' + config['name']
    logging_path = root_path + '/' + config['name']
    
    # Start logging
    print("Start training model: " + model_name)
    print("Configuration: {} hidden layers containing {} neurons".format(config['num_layers'], config['num_units']))
    print("Training set: {} examples".format(train_size))
    print("Validation set: {} examples".format(val_size))
    
    # Create logging directory
    get_ipython().system('mkdir -p $logging_path')
    # Remove prior logs
    get_ipython().system('rm $logging_path/*')
    
    # load and save model
    model = classification_model(features.shape[1], num_classes, config['num_layers'], config['num_units'])
    save_architecture(model, model_path + '.json')
    
    # load model callbacks
    cbs = get_callbacks(model_name=model_name, log_dir=logging_path, verbose=1)
    
    # train model
    model.fit(features[:train_size], 
          oh_labels[:train_size], 
          validation_data=(features[-val_size:], oh_labels[-val_size:]), 
          batch_size=batch_size, 
          epochs=100, 
          verbose=0,
          shuffle=True,
          callbacks=cbs)
    
    # print best result
    history = cbs[2]
    print_classification_metrics(history)
    
    # add newline after model was trained
    print('\n')

print("END MODEL TRAINING")
