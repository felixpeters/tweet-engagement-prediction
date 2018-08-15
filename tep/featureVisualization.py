class FeatureVisualizer():
    """
    Class for interpreting learned features in DNNs trained on NLP tasks.
    """ 

    def __init__(self, model, word_index):
        self.model = model
        self.word_index = word_index

    def analyze_example(seq, layer, num_results=10):
        """
        Examines one specific example, looking for the highest activations
        across filters and positions.

        Args:
           seq: Example to analyze, given as sequence of word IDs
           layer: Network layer to examine, identified by name
           num_results: Integer stating how many results should be returned
        Returns:
            Tuple activations, filters and corresponding words
        """
        return

    def analyze_neuron(batch, layer, neuron, num_results=10):
        """
        Examines one specific neuron, looking for the highest activations
        across given examples and positions.

        Args:
            batch: Examples to examine, given as array of sequences
            layer: Network layer to examine, identified by name
            neuron: Integer identifying the neuron to examine
            num_results: Integer stating how many results should be returned
        Returns:
            Tuple of activations, examples and corresponding words
        """
        return
