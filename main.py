import numpy as np

def cond_probability(word1, word2):
    '''
    Function that calculates the conditional probability P(word2 | word1)

    Parameters
    ----------
    word1 : Preceding word
    word2 : Successive word
    '''
    global word_count
    global word_pairs

    probability = word_pairs[(word1, word2)] / word_count[word1]
    return probability

if __name__ == "__main__":
    word_count = dict()
    word_pairs = dict()

    # Obtain word counts and word pairs
    sentences_file_path = 'sentences.txt'
    with open(sentences_file_path, 'r') as sentences:
        for sentence in sentences:
            words = sentence.strip().split()
            # Obtain word counts
            for i in words:
                if i not in word_count: # Initialize key
                    word_count[i] = 0
                word_count[i] += 1

            # Obtain word pairs that come consecutively
            for i in range(len(words) - 1):
                word_pair = (words[i], words[i + 1])
                if word_pair not in word_pairs:
                    word_pairs[word_pair] = 0
                word_pairs[word_pair] += 1

    sentence = list()
    token = '<|start|>' # Sentences start with this token
    while token != '<|end|>':
        sentence.append(token)
        next_word_candidates = dict()   # Store candidate next words and their conditional probabilities
        for pair in word_pairs.keys():
            if pair[0] == token:
                next_word_candidates[pair[1]] = cond_probability(token, pair[1])

        # Apply random sampling based on the conditional probability distribution
        token = np.random.choice(list(next_word_candidates.keys()), p=list(next_word_candidates.values()))
    
    sentence.append(token)
    print(' '.join(sentence))
