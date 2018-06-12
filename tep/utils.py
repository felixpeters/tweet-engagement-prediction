import json
import bcolz
import numpy as np
import pandas as pd
from datetime import tzinfo, timedelta
from dateutil.parser import parse

ZERO = timedelta(0)
HOUR = timedelta(hours=1)

def class_distribution(data, title, normalize=False, sort=False):
    """
    Return value counts (or percentages) for the given discrete distribution.
    """
    df = pd.DataFrame(data=data, columns=[title])
    df = df[title].astype('category')
    counts = df.value_counts(sort=sort, normalize=normalize)
    return counts

def discretize(data, boundaries):
    """
    Discretize a continuous distributions into classes according to the given
    boundaries.
    """
    classes = np.empty(len(data))
    for i, count in enumerate(data):
        for j, upper_bound in enumerate(boundaries):
            if count <= upper_bound:
                classes[i] = int(j)
                break
        else:
            classes[i] = len(boundaries)
    return classes

def save_as_json(data, filename):
    """
    Save the given piece of data in JSON format to the given file.

    Args:
        data: Array of twitter.models.* instances
        filename: string
    """
    with open(filename, 'w') as f:
        for d in data:
            json.dump(d.AsDict(), f, sort_keys=True)
            f.write("\n")
    return

def save_as_text(data, filename):
    """
    Save the given data to a file, separated by newlines
    """
    with open(filename, 'w') as f:
        for d in data:
            f.write(d.encode('unicode_escape').decode())
            f.write("\n")
    return

def save_array(array, filename):
    """
    Save numpy array to file in compressed form.
    """
    c = bcolz.carray(array, rootdir=filename, mode='w')
    c.flush()
    return

def load_array(filename):
    """
    Load numpy array from file.
    """
    return bcolz.open(filename)[:]

def is_newer_than(tweet, date):
    """
    Determines whether tweet was created after given date.

    Args:
        tweet: twitter.models.Status instance
        date: datetime, non-naive (meaning with timezone info)
    Returns:
        Boolean
    """
    return parse(tweet.created_at) > date
    
def is_older_than(tweet, date):
    """
    Determines whether tweet was created before given date.

    Args:
        tweet: twitter.models.Status instance
        date: datetime, non-naive (meaning with timezone info)
    Returns:
        Boolean
    """
    return parse(tweet.created_at) < date

class UTC(tzinfo):
    """ UTC helper class """

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO
