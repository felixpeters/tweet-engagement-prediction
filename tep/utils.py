import json

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
