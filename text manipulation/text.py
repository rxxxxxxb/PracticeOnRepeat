import string


def load_words():
    words = {}
    exclude = set(string.punctuation + "\n") #exlude the . , #$% in an essay. 
    print(exclude)
    word_count = 0

    with open("tale-of-two-cities.txt", "r") as content:
        for line in content:
            line = line.replace("--", ' ')
            line_words = line.split(" ")
            for word in line_words:
                word = ''.join(char for char in word if char not in exclude)
              
                # add to dict and keep track of times it occurs
                if word:
                    word = word.lower()
                    word_count += 1
                   
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
                    
    return words

def main():
    words = load_words()
    word_count = len(words)
    print(word_count)

main()    
