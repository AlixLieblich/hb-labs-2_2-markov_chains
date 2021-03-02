"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read() # if theres an error it might be because of line breaks

    return contents

# print(open_and_read_file('green-eggs.txt'))    

def make_chains(text_string):

    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = contents.split()

    for i in range(len(words) - 2):
        
        # tuple(phrase) = words[i], words[i+1]
        # chains[phrase] = [] ## phrases is our key; empty list is our values ### may be unneeded :-)
        # list[occurances] ## intialize an empty list for our values
        # list.append(words[i + 2]) ## appened all words[i + 2] to the list
        # chains[phrase] = chains[list] ## append the list of values to its phrase in dict chains

        key_phrases = (words[i], words[i+1]) # ex: ('Would', 'you') ## type tuple
        value_word = words[i + 2] # ex: 'could' ## type string
     

        if key_phrases not in chains: # if the var key_phrases is not already a key in our dict, chains:
            chains[key_phrases] = []  # set key_phrases as a key in our dict, chains, set to a value ## type empty list

        chains[key_phrases].append(value_word) # appending value_word (type string) to value (type list) 
                                               # for the key value pair where key is key_phrases (type tuple)
                                               
    return chains
# print(make_chains(contents))

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
contents = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(contents)

# Produce random text
random_text = make_text(chains)

print(random_text)
