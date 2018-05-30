import re
    
def hashtag_repl(hashtag):
    body = hashtag.group(0)[1:]
    if body.upper() == body:
        result = '<hashtag> ' + body + ' <allcaps>'
    else:
        result = ' '.join(['<hashtag>'] + re.findall(r'[a-zA-Z][^A-Z]*', body))
    return result
    
def repeat_repl(punctuation):
    return punctuation.group(1) + ' <repeat>'

def punctuation_repl(punctuation):
    return ' ' + punctuation.group(0)
    
def elong_repl(match):
    return match.group(1) + match.group(2) + ' <elong>'
    
def allcaps_repl(match):
    match = match.group(0)
    return match.lower() + ' <allcaps>'

def tokenize(input):
    """
    Marks and/or replaces occurrences of recurring patterns such as URLs, 
    numbers etc.
    
    Args:
        input: string
    Returns:
        Tokenized string
    """
    # mark URLs
    input = re.sub(r'https?:\/\/\S+\b|www\.(\w+\.)+\S*', '<url>', input)
    # split words appended with slashes (after tokenizing URLs ;-))
    input = re.sub(r'/', ' / ', input)
    # mark user mentions
    input = re.sub(r'@\w+', '<user>', input)
    # replace emojis
    input = re.sub(r'[8:=;][\'\\-]?[)d]+|[)d]+[\'\\-]?[8:=;]', '<smile>', input, flags=re.IGNORECASE)
    input = re.sub(r'[8:=;][\'\\-]?p+', '<lolface>', input, flags=re.IGNORECASE)
    input = re.sub(r'[8:=;][\'\\-]?\(+|\)+[\'\\-]?[8:=;]', '<sadface>', input)
    input = re.sub(r'[8:=;][\'\\-]?[\/|l*]', '<neutralface>', input)
    input = re.sub(r'<3', '<heart>', input)
    # replace numbers
    input = re.sub(r'[-+]?[.\d]*[\d]+[:,.\d]*', '<number>', input)
    # split hashtags on uppercase letters
    input = re.sub(r'#\S+', hashtag_repl, input)
    # mark punctuation repetitions
    input = re.sub(r'([!?.]){2,}', repeat_repl, input)
    # add spaces around punctuation
    input = re.sub(r'([!?.])', punctuation_repl, input)
    # mark elongated words
    input = re.sub(r'\b(\S*?)(.)\2{2,}', elong_repl, input)
    # mark allcaps words
    input = re.sub(r'([A-Z]{2,})', allcaps_repl, input)
    # filter unicode characters
    #input = input.decode('unicode_escape', 'ignore').encode('ascii', 'ignore')
    return input.lower()
