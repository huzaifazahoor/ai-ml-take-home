"""
This question was to make BPE tokenizer,
so BPE have two parts, one is training and second is encoding,
so in training part, we need to find the most frequent pair of characters in the corpus,
and then we need to merge that pair and then we need to repeat this process for the number of merges,
and in encoding part, we need to encode the word using the merges we got from training part

So i tried to do it, but i was not be able to do it properly,
i was stuck on the part like how to get the characters of the word after merging,
same thing happened in encoding part,
so the output is not same,

but i understand now the logic of BPE, i spent too much time on it,
So i shifted my focus to next question
"""


def train(corpus, num_merges):
    # question have constraints on the corpus length
    if len(corpus) < 1 or len(corpus) > 5000:
        raise ValueError("Corpus length must be between 1 and 5000")

    # question have constraints on the number of merges
    if num_merges < 1 or num_merges > 5000:
        raise ValueError("num_merges must be between 1 and 5000")

    merges = []
    for _ in range(num_merges):

        pairs = list()

        for word, freq in corpus:

            # question have constraints on the word length
            if len(word) < 1 or len(word) > 40:
                raise ValueError("Word length must be between 1 and 40")

            characters = list()
            # here i tried different ways to get the characters of the word,
            # but i was not able to get it properly
            # for w in word:
            # for merge_word in merges:
            # if merge_word in w:
            # w = w.replace(merge_word, "")
            # characters.append(w)

            if len(merges) > 0:
                for merge_word in merges:
                    if merge_word in word:
                        pos = word.index(merge_word)
                        characters = list(word)

                        # here same way, i was not able to get it properly,
                        # but i understand the logic of BPE
                        # we need to do it same here like we did in encode
                        # so this way is pending

                        characters[pos] = merge_word
                        characters.pop(pos + 1)
                        # list(word[:pos]) + [merge] + list(word[pos + len(merge):])

            if len(characters) == 0:
                # only doing it for first time,
                # because after that we will have merges
                characters = list(word)

            for i in range(len(characters) - 1):

                pair = (characters[i], characters[i + 1])
                pairs.append(pair)

        frequency_dict = {}

        for pair in pairs:

            continuous_pair = pair[0] + pair[1]

            # find pair in words
            for word, freq in corpus:
                if continuous_pair in word:

                    # summing the frequency of the pair in the corpus
                    frequency_dict[continuous_pair] = (
                        frequency_dict.get(continuous_pair, 0) + freq
                    )

        # getting first using tie-breaking method,
        # because max function will return the first maximum value in case of tie
        max_frequency_pair = max(frequency_dict, key=frequency_dict.get)

        merges.append(max_frequency_pair)

    return list(set(merges))


def encode(word, merges):
    new_word = list(word)

    for merge_tuple in merges:

        # combining it to check that if it is in the word or not,
        # because merge_tuple is a tuple of two characters
        merge = merge_tuple[0] + merge_tuple[1]

        if merge in word:

            pos = word.index(merge)
            # this way, it will set in the position where it is needed.
            new_word = list(word[:pos]) + [merge] + list(word[pos + len(merge) :])

    return list(new_word)


if __name__ == "__main__":
    # using the original input from the question
    corpus = [
        ("low", 5),
        ("lower", 2),
        ("newest", 6),
        ("widest", 3),
    ]
    num_merges = 4
    merges = train(corpus, num_merges)
    # this output is not same as the original one,
    # because i was not be able to solve it properly
    # but i understand actually how BPE works
    print("Merges:", merges)

    word = "lower"
    # took expected merges from the question,
    # because my output is not same as the original one
    expected_merges = [("e", "s"), ("es", "t"), ("l", "o"), ("lo", "w")]
    encoded_word = encode(word, expected_merges)
    print("Encoded word:", encoded_word)
