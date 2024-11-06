words_array = ["the", "sky", "is", "blue"]
lengths_array = [3,2,2,1]

def rebuild_sentence(words, lengths):
    output = ""
    
    for i in range(len(words)):
        for j in range(lengths[i]):
            
            # hanling numbers greater than length of a word
            if j<len(words[i]):
                output= output+words[i][j]
                
        output= output+" "
    print(output)

rebuild_sentence(words_array, lengths_array)
    
            
        