from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

class EmbeddingGenerator():
    """
    Class for preparing preprocessed texts into sequences and creating an
    embedding matrix.
    """

    def __init__(self):
        self.word_index = {}
        self.embeddings_index = {}
        self.embedding_dimension = 0
        self.tokenizer = Tokenizer(num_words=None, filters='\t\n\\')

    def generate_word_index(self, texts):
        """
        Creates the word index from the given texts.
    
        Args:
            texts: Array of strings
        Returns:
        The generated word index
        """
        self.tokenizer.fit_on_texts(texts)
        self.word_index = self.tokenizer.word_index
        return self.word_index
    
    def generate_sequences(self, texts, maxlen=32):
        """
        Transforms texts into sequences of word indices.
        Pads sequences so that they have equal length.
        Only callable after word index was generated.
    
        Args:
            texts: Array of strings
        Returns:
            The padded sequences as a 2D-array of strings
        """
        sequences =  self.tokenizer.texts_to_sequences(texts)
        return pad_sequences(sequences, maxlen=maxlen)
    
    def load_pretrained_embedding(self, filename):
        """
        Loads a pretrained embeddings index from the given file.
        Assumes a file with one line per embedding, starting with word and
        followed by coefficients (separated by spaces).
    
        Args:
            filename: Path to embedding
        Returns:
            The loaded embeddings index
        """
        f = open(filename, encoding='utf-8')
        coefs = [] 
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            self.embeddings_index[word] = coefs
        f.close()
        self.embedding_dimension= len(coefs)
        return self.embeddings_index
    
    def generate_embedding_matrix(self):
        """
        Creates embedding matrix from word and embeddings indices.
    
        Returns:
            Generated embedding matrix as 2D numpy array
        """
        embedding_matrix = np.zeros((len(self.word_index) + 1, self.embedding_dimension)) 
        for word, i in self.word_index.items():
            embedding_vector = self.embeddings_index.get(word)
            if embedding_vector is not None:
                # words not found will stay all-zeros
                embedding_matrix[i] = embedding_vector
        return embedding_matrix
