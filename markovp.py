import os
import random

from hashtable import HashTable
from wordObj import wordObj

def build_lexicon(input_filename, lexicon): #Analyse the text file and populate a hashtable with relevant data
    wordCount = 0
    uniqueCounter = 0
    with open(input_filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
        
            for i, word in enumerate(words):
                if len(word) == 0:
                    continue  # skip current iteration if the word is empty

                # try to find the following word
                try:
                    nextword = words[i + 1]
                    print(f"Word \"{word}\" is followed by \"{nextword}\"")
                except IndexError:
                    print(f"Word \"{word}\" is at the end of the text! -------------")
                    nextword = None

                    #add current word to the table (if it doesnt already exist)
                    #if it does exist, increment the frequency
                    #in either case, we then add the next word to that word's followingWords list

                wordObject = wordObj(word)
                    
                idx = lexicon.search(wordObject) #return index of the word if it exists in table
                if idx == -1: #-1 returned if word doesnt exist in table
                    wordObject.followingWords.append(nextword)
                    lexicon.insert(wordObject)
                    uniqueCounter += 1

                else:
                    lexicon.data[idx].frequency += 1
                    lexicon.data[idx].followingWords.append(nextword)

                wordCount += 1
                
        file.close()
        lexicon.print()
        print(f"Total corpus words parsed: {wordCount}")
        print(f"Total unique words parsed: {uniqueCounter}")
        print(f"Writing corpus analysis to file for debugging purposes.")

        with open("corpusdebug.txt", 'w', encoding='utf-8') as file:
            for i in range(lexicon.size):
                if lexicon.data[i] != lexicon.unoccupied:
                    file.write(str(lexicon.data[i]) + "\n")
        file.close()
        print("Corpus analysis completed.")

def MarkovP(output_filename, lexicon, desired_length):
    #the hashtable most likely contains a lot of empty values, which are represented as "-1"
    #to more efficiently process data, we will create a new list containing only the words that have been inserted

    def get_starter(lexicon):
        choice = random.choice( [word for word in lexicon] ) #pick a random word 
        return choice

    print("Beginning Markov generation.")
    lexiconList = []
    outputString = ""

    #perhaps inefficient and linear, but all values in the hashtable have to be checked once anyway
    for i in range(lexicon.size):
        if lexicon.data[i] != lexicon.unoccupied:
            lexiconList.append(lexicon.data[i])

    starter = get_starter(lexiconList)
    currentWord = starter
    outputString += starter.spelling + " "

    words = 0
    while words < desired_length:

        nextWord = random.choice( currentWord.followingWords ) 
        print(f"Current word: {currentWord.spelling}, Next word: {nextWord}") #this can get a little bit confusing. nextword is whatever we're about to append

        if nextWord == None:
            seed = get_starter(lexiconList)
            nextWord = seed.spelling
            print("Reseeding because the word didn't have any words following it. New seed: {seed.spelling}")
        
        outputString += nextWord + " "

        #find next word as an object, so we can find its following words for the next iteration
        #the next word of this object becomes the current word for the next iteration!
        for word in lexiconList:
            if word.spelling == nextWord:
                currentWord = word

        words += 1

    print(outputString)

    print(f"Writing to file {output_filename}...")
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(outputString)
    file.close()
    print("Markov generation complete.")

htable = HashTable() #instantiate empty hashtable

input_filename = input("Enter filename containing text corpus (suggested: gutenberg.txt): ")
output_filename = input("Enter filename for generated text output: ")
desired_length = int(input("Enter desired length of generated text in words (suggested: 200): "))

if not os.path.isfile(input_filename):
    print(f"File {input_filename} could not be opened, or was not found.")
    print("Exiting...")
    exit()

build_lexicon(input_filename, htable) #Analyse text corpus and populate hashtable
MarkovP(output_filename, htable, desired_length) #Generate markov chain and write to output file