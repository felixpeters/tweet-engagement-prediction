import numpy as np
from .tweetPreprocessor import tokenize
from .featureGenerator import FeatureGenerator
from .labelGenerator import LabelGenerator

class DataPreprocessor():
    """
    Class for extracting features and labels from raw tweet objects
    """

    def extract_content(self, tweets):
        """
        Extracts the tweet text and preprocesses it according to GloVe embedding
        specification.

        Args:
            tweets: Array of twitter.models.Status instances
        Returns:
            Array of tokenized strings
        """
        result = []
        for t in tweets:
            text = t.text
            result.append(tokenize(text))
        return result

    def extract_additional_features(self, tweets):
        """
        Extracts additional information from tweet objects, such as number of
        followers, friends, account age etc.

        Args:
            tweets: Array of twitter.models.Status instances
        Returns:
            2D-numpy array with additional features for each tweet
        """
        fg = FeatureGenerator()
        result = np.zeros((len(tweets), len(fg.structured_features)))
        for i, t in enumerate(tweets):
            features = fg.extract_structured_features_for_tweet(t)
            result[i] = features
        return result

    def extract_labels(self, tweets, classes=None):
        """
        Extracts labels (i.e. retweet statistics) from raw tweet 
        objects. If no classes are delivered, counts are returned for a
        regression model.

        Args:
            tweets: Array of twitter.models.Status instances
            classes: Buckets for classification
        Returns:
            Numpy array containing retweet statistics for each tweet.
        """
        lg = LabelGenerator()
        result = np.zeros(len(tweets))
        if classes is not None:
            result = lg.generate_retweet_classes(tweets, classes)
        else:
            result = lg.generate_retweet_counts(tweets)
        return result

