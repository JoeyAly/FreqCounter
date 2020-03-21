import string

# Starting number for alpha characters
STARTING_ALPHABET_POS = 97


def countWords(fname):

    exclude = set(string.punctuation)

    diction = {}

    # Go through each line from text
    # Clean up each word and add it to dictionary. If it exists increment the value by 1.
    for line in fname:
        words = line.lower().strip().split()
        for w in words:
            word = ''.join(ch for ch in w if ch not in exclude)


            diction[word] = diction.get(word, 0) + 1

    # Sort items by value in reverse order
    sortedDictByValue = sorted(diction.items() , reverse=True, key=lambda item: item[1])
    return sortedDictByValue


# Convert each character into unicode and
def countCharacters(text):

    results = [0] * 26

    for char in text:
        if char.isalpha():
            char_val = ord(char) - STARTING_ALPHABET_POS # 0
            results[char_val] += 1
    return results



fname = open('turing.txt','r')
sortedDictByValue = countWords(fname)

for item in sortedDictByValue:
    print("{} {}".format(item[0], item[1]))

#for key, value in sortedDictByValue:
#    print("{} {}".format(key, value))

print("")

text = open('turing.txt','r').read().lower()

results = countCharacters(text)

for index in range(0, len(results)):
    print("{} = {}".format(chr(index + STARTING_ALPHABET_POS), results[index]))

fname.close()






