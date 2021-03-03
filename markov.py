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
# PSEUDOCODE:
        # tuple(phrase) = words[i], words[i+1]
        # chains[phrase] = [] ## phrases is our key; empty list is our values ### may be unneeded :-)
        # list[occurances] ## intialize an empty list for our values
        # list.append(words[i + 2]) ## appened all words[i + 2] to the list
        # chains[phrase] = chains[list] ## append the list of values to its phrase in dict chains

# BEGIN CODE: 

    chains = {}
    words = contents.split()
    words.append(None)


    for i in range(len(words) - 2): # needs to be 2 less than length of words (type list) because will get out of range for index for words[i + 2]

        key_phrases = (words[i], words[i+1]) # ex: ('Would', 'you') ## type tuple
        value_word = words[i + 2] # ex: 'could' ## type string ### for last iteration, for key, value pair ('I', 'am?'), word[i + 2] is None (because with appended None to the end of the list)
     

        if key_phrases not in chains: # if the tuple key_phrases is not already a key in our dict, chains:
            chains[key_phrases] = []  # set key_phrases as a key in our dict, chains, set to a value of an empty list

        chains[key_phrases].append(value_word) # appending value_word (type string) to the value of our key, value pair (of type list) 
                                               # for the key value pair where key is key_phrases (type tuple)

    return chains
# print(make_chains(contents))

def make_text(chains):
    """Return text from chains."""
# PSEUDOCODE:
    #from chains(dictionary) use choice to select a key # (word 1, word 2)
    #   words.append((word1,word2))
    #use choice to select a value from key value pair  # word 3
    #   words.append(word)
    #new_key = (key[1],value)  # word 2, word 3
    #search dictionary for new_key
    #   use choice to select a value from key value pair
    #Method #1 : Using random.choice() + list() + items()
        #random key ('a','b') : ['random value' 'c']
    # The combination of above methods can be used to perform this task. The choice function performs the task of random value selection and list method is used to convert the pairs accessed using items() into a list over which choice function can work.

    # new key ('b','random value') : ['n','l']
    # next new key ('random value', 'l') : ...


# BEGIN CODE:

    words = [] # initializing an empty list, words
    key_phrase = choice(list(chains.keys())) # get a random choice from the list of all keys from the dict, chains and set it to var key_phrase (type tuple)
    words.append(key_phrase[0]) # add first word of key_phrase to words
    words.append(key_phrase[1]) # add second word of key_phrase to words
    value_word = choice(chains[key_phrase]) # get a random choice from the list of values stored at the key called key_phrase and set it to var value_word (type string)
    
# loop through dict looking for key_phrase tuples; when value_word = None (from appending None in make_chains), stop the loop
    while value_word is not None: 
    # set the second word of tuple, key_phrase (created above), and value_word (created above) to the variable name 'key_phrase,' (type tuple)
        key_phrase = (key_phrase[1], value_word) 
    # add value_word to words (type list)
        words.append(value_word) 
    # get a random choice from the list of values stored at the key called key_phrase
    # look up key, called key_phrase (type tuple), within chains (type dict), in order to use random choice (type method) to return one value from the list stored in the key, value pair, and store it to the variable name 'value_word' (type string)
        value_word = choice(chains[key_phrase]) 

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
contents = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(contents)

# Produce random text
random_text = make_text(chains)

print(random_text)
