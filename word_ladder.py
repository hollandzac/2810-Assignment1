#! /usr/bin/env python3
import re
#Computes the length of a list made by the each letter for item that is the same
#as the target in the same position
def same(item, target):
    #using the zip function to iterate over each index in item and target at the
    #same time if equal add to list then retun length
    return len([c for (c, t) in zip(item, target) if c == t])

#This function builds a list by searching the words list and if word
# not in seen or list and the regex search returns !None
def build(pattern, words, seen, wordList, noAllow):
    #the re search '.' character in pattern matches any character except newline
    #will return true as long as all other characters match plus any letter in the
    # '.' postiion
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in wordList and word not in noAllow]

#finds the path to the target word
def find(word, words, seen, target, path, noAllow):
    wordList = list()
    #for each letter in curren word replace it with '.' character and call build function
    #with that pattern append that list to wordList
    for i in range(len(word)):
        wordList += build(word[:i] + "." + word[i + 1:], words, seen, wordList, noAllow)

    #If no words found to change to remove word from path return false
    if len(wordList) == 0:
        return False

    #sorts word list into tuples of (number of matches with target word, word) in descending order
    # of  matches
    wordList = sorted([(same(w, target), w) for w in wordList], reverse=True)

    # for each tuple in wordList if match is 1 off length of word a path has been found
    #add word to path and return true if not add word as key in seen
    for (match,item) in wordList:
        if match == len(target) - 1:
            path.append(item)
            return True
        seen[item] = True


#if path is not completed appends the closest matching item to path and recursively
#calls find with the closest match being the new word
#if the match is no closer retuns false which will remove last entry from path
    for (match, item) in wordList:
        if match==0:
            return(False)
        path.append(item)
        if find(item, words, seen, target, path, noAllow):
            return True
        path.pop()

#Takes dictionary file name as input then opens it
fname = input("Enter dictionary name: ")#dictionary file name
while fname[-4:] != '.txt':
    fname = input("Dictionary must be .txt file : ")

file = open(fname)
lines = file.readlines() #each line in file
#list of words not to be used
noAllow = [x for x in input("Enter list of words not allowed seperated by a white space: ").split()]
start = input("Enter start word:") #starting word
words = [] #list of all words of the same length  in dictionary


#iterates of each line in file strips white space off end
for line in lines:
    word = line.rstrip()
    #if anyword same length as start word add to list
    if len(word) == len(start):
      words.append(word)
target = input("Enter target word:") #target word


path = [start]#stores the ordered path to target word
seen = {start : True} # dictionary for seen wor

#Once find calculates the path and returns True prints shortest path length and path
#else no path found
if find(start, words, seen, target, path, noAllow):
  path.append(target)
  print('Shortest path is: ',len(path) - 1, path)
else:
  print("No path found")
