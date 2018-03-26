import json
import difflib
data = json.load(open("data.json")) #reads the json file

def main(word): #main dictionary fucntion
    word = word.lower()#converts every word entered, into a lower case word
    if word in data:
        return data[word]
    else:
        for d in data:
            diff = difflib.SequenceMatcher(None, word, d)
            percent_diff = diff.ratio()*100
            percent_diff = round(percent_diff,1)
            percent_diff = str(percent_diff)

#            return percent_diff

        close_match = difflib.get_close_matches(word, d, 1, 0.8)
        return close_match
#        for match in close_match:
#                return data[match]



get_word = input("Enter the word: ")
print(main(get_word))
