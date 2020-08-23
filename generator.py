
"""
File name : generator.py
Author's name : Seyeong Park
Student Number : 301088175
File description : This is the main python file. Generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random.
"""

import random

def getWord(filename):
    # open an input file with this name
    inFile = open(filename,'r')

    # define a temporary list
    temList = [word.strip() 

    #read words from the file
    for word in inFile.readlines()]

    # convert the list to a tuple 
    tupList = tuple(temList)

    # close to the file
    inFile.close()

    # return this tuple
    return tupList

# add them to the list
nouns = getWord('nouns.txt')
verbs = getWord('verbs.txt')
articles = getWord('articles.txt')
prepositions = getWord('prepositions.txt')
conjunction = getWord('conjunction.txt')
adjective = getWord('adjective.txt')

def sentence():
    """Builds and returns a sentence, conjunction, and a second independent clauss"""
    return "\n"+nounPhrase() + " " + verbPhrase() +" "+ conjunctionPhrase()+" "+nounPhrase() + " " + verbPhrase() +"\n"

def nounPhrase():
    """Builds and returns a noun phrase. If the random article is 'a', it will not add adjective"""
    randomArticle=random.choice(articles)
    if randomArticle=="A":
        return randomArticle + " " + random.choice(nouns)
    else:
        return randomArticle + " "+random.choice(adjective)+" " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def conjunctionPhrase():
    """Builds and returns a conjunction phrase."""
    return random.choice(conjunction)

def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("\nEnter the number of sentences: "))
    for count in range(number):
        print(sentence())
        
main()
