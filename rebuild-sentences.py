"this function rebuild a words of a list accordin to a specific length"

WORDS_ARRAY = ["the", "sky", "is", "blue"]
lengths_array = [3,2,2,1]

def _rebuild_sentence(words, lengths):
    length_of_array = len(words)
    output = ""

    for i in range(length_of_array):
        for j in range(lengths[i]):

            # hanling numbers greater than length of a word
            if j<len(words[i]):
                output= output+words[i][j]

        output= output+" "
    print(output)

_rebuild_sentence(WORDS_ARRAY, lengths_array)
