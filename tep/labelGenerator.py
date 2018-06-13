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
                count = t.retweet_count or 0
                if count <= upper_bound:
                    labels[i] = int(j)
                    break
            else:
                labels[i] = len(buckets)
        return labels
