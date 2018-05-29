import json
from datetime import tzinfo, timedelta
from dateutil.parser import parse

ZERO = timedelta(0)
HOUR = timedelta(hours=1)

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
            f.write(str(d))
            f.write("\n")
    return

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
