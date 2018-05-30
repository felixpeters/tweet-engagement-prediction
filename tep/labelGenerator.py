import twitter
import numpy as np

class LabelGenerator():
    """
    Class for extracting labels from tweet objects.
    """

    def generate_retweet_counts(self, tweets):
        """
        Returns retweet counts suited for regression models.

        Args:
            tweets: Array of twitter.models.status instances
        Returns:
            Numpy array with retweet counts for the given tweets
        """
        labels = np.array([t.retweet_count or 0 for t in tweets])
        return labels

    def generate_retweet_classes(self, tweets, buckets):
        """
        Returns labels as class numbers for the given buckets.

        Args:
            tweets: Array of twitter.models.status instances
            buckets: Array of upper bounds (inclusive) for buckets
        Returns:
            Numpy array of class labels (beginning at 1) for the given tweets
        """
        labels = np.empty(len(tweets))
        for i, t in enumerate(tweets):
            for j, upper_bound in enumerate(buckets):
                if t.retweet_count <= upper_bound:
                    labels[i] = int(j)
                    break
            else:
                labels[i] = len(buckets)
        return labels

    def one_hot_encoding(self, class_labels, number_classes):
        """
        Returns one-hot encoded class labels.

        Args:
            class_labels: Array of class labels
            number_classes: Number of buckets
        Returns:
            Numpy array of one-hot encoded label rows
        """
        labels = np.zeros((len(class_labels), number_classes)) 
        for index, class_label in enumerate(class_labels):
            labels[index, int(class_label)] = 1
        return labels
