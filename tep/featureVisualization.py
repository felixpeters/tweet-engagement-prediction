import operator
from keras.models import Model
import numpy as np

class ConvLayerVisualizer():
    """
    Class for interpreting learned features in the first convolutional layer
    of a network trained on an NLP task.
    """ 

    def __init__(self, model, word_index):
        self.model = model
        sorted_word_tuples = sorted(word_index.items(), key=operator.itemgetter(1))
        sorted_words = [t[0] for t in sorted_word_tuples]
        self.sorted_words = ['<unknown>'] + sorted_words

    def analyze_example(self, seq, layer, num_results=10):
        """
        Examines one specific example, looking for the highest activations
        across filters and positions.

        Args:
           seq: Example to analyze, given as sequence of word IDs
           layer: Convolutional layer to examine, identified by name
           num_results: Integer stating how many results should be returned
        Returns:
            Tuple of activations, filters and corresponding words
        """
        kernel_size = self.model.get_layer(layer).kernel_size[0]
        activations = np.squeeze(self.get_activations(layer, np.expand_dims(seq, axis=0)))
        sorted_activations = np.argsort(activations, axis=None)
        xs, ys = np.unravel_index(sorted_activations, activations.shape)
        sorted_idx = np.flip(list(zip(xs, ys)), axis=0)[:num_results]
        results = []
        for idx in sorted_idx:
            result = {
                'activation': activations[idx[0], idx[1]],
                'kernel': idx[1],
                'position': idx[0],
                'words': self.get_words(seq, idx[0], kernel_size),
            }
            results.append(result)
        return results

    def analyze_neuron(self, batch, layer, neuron, num_results=10):
        """
        Examines one specific neuron, looking for the highest activations
        across given examples and positions.

        Args:
            batch: Examples to examine, given as array of sequences
            layer: Convolutional layer to examine, identified by name
            neuron: Integer identifying the neuron to examine
            num_results: Integer stating how many results should be returned
        Returns:
            Tuple of activations, examples and corresponding words
        """
        kernel_size = self.model.get_layer(layer).kernel_size[0]
        window_size = kernel_size
        activations = self.get_activations(layer, batch)
        neuron_activations = activations[:,:,neuron]
        sorted_activations = np.argsort(neuron_activations, axis=None)
        xs, ys = np.unravel_index(sorted_activations, neuron_activations.shape)
        sorted_idx = np.flip(list(zip(xs, ys)), axis=0)[:num_results]
        results = []
        for idx in sorted_idx:
            result = {
                'activation': neuron_activations[idx[0], idx[1]],
                'kernel': neuron,
                'tweet': idx[0],
                'position': idx[1],
                'words': self.get_words(batch[idx[0]], idx[1], kernel_size),
            }
            results.append(result)
        return results

    def get_activations(self, layer, batch):
        """
        Retrieve hidden layer activations for a batch of examples.

        Args:
            layer: Name of the hidden layer
            batch: Array of sequences for which activations are calculated
        Returns:
            Multidimensional array of activations
        """
        temp_model = Model(inputs=self.model.input, outputs=self.model.get_layer(layer).output)
        activations = temp_model.predict(batch)
        return activations

    def get_words(self, sequence, position, kernel_size):
        """
        Lookup words for the given position in the given sequence using the
        word index.
        Sequence is zero-padded according to the given kernel size.
        """
        pad_size = int(np.floor(np.divide(kernel_size, 2)))
        padded_seq = np.pad(sequence, pad_size, 'constant', constant_values=0)
        word_ids = padded_seq[position:(position + kernel_size)]
        words = []
        for word_id in word_ids:
            word = self.lookup_word(word_id)
            words.append(word)
        return " ".join(words)

    def lookup_word(self, word_id):
        return self.sorted_words[word_id]
