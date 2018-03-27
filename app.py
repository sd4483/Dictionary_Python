import json
import difflib
data = json.load(open("data.json")) #reads the json file

def main(word): #main dictionary fucntion
    word = word.lower()#converts every word entered, into a lower case word
    if word in data:
        return data[word]
    elif word.title() in data:#this checks for words with capital letters at the beginning
        return data[word.title()]
    else:
        close_match = difflib.get_close_matches(word, data.keys(), 1, 0.8) #Checks if there any close matches with the dict keys
        if len(close_match)>0:
            verify_match = input("Did you mean " + close_match[0] + " : yes/no \n") #asks the user, if that is the word he wants the meaning of
            if verify_match == 'yes':
                return data[close_match[0]]
            elif verify_match == 'no':
                return "Sorry, couldn't find the word"
            else:
                print("We couldn't understand the entry")
        else:
            return "Please check the word"

get_word = input("Enter the word: ")

output = main(get_word)#appending the output to a list

if type(output) == list:
    for i in output:#iterating the list to print in lines
        print(i)
else:
    print(output)
