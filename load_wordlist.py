

def load_words(file_name):
    print("Loading word list from file...")
    wordlist = list()
    with open(file_name) as file:
        for line in file:
            wordlist.append(line.rstrip('\n'))
        print(" ", len(wordlist), "words loaded.")
        return wordlist



