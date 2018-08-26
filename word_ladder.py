#! /usr/bin/env python3
import re
#Computes the length of a list made by the each letter for item that is the same
#as the target in the same position
def same(item, target):
    #using the zip function to iterate over each index in item and target at the
    #same time if equal add to list then retun length
    return len([c for (c, t) in zip(item, target) if c == t])

#This function builds a list by searching the words list and if word
# not in seen or list and the regex search returns true
def build(pattern, words, seen, wordlist):
    #the re search '.' character in pattern matches any character except newline
    #will return true as long as all other characters match plus any letter in the
    # '.' postiion
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in wordlist]

#finds the path to the target word
def find(word, words, seen, target, path):
  wordlist = list()
  #for each letter in curren word replace it with '.' character and call build function
  #with that pattern append that list to wordlist
  for i in range(len(word)):
    wordlist += build(word[:i] + "." + word[i + 1:], words, seen, wordlist)
    print(wordlist)

  #If no words found to change to remove word from path return false
  if len(wordlist) == 0:
      path.pop()
      print('blue')
      return False
#sorts word list into tuples of (number of matches with target word, word) in descending order
# of  matches
  wordlist = sorted([(same(w, target), w) for w in wordlist], reverse=True)
  print(wordlist)

# for each tuple in wordlist if match is 1 off length of word a path has been found
#add word to path and return true if not add word as key in seen
  for (match, item) in wordlist:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
        #print(path)
      return True
    seen[item] = True
    print('hi')
    #print(seen)


  for (match, item) in wordlist:
      if match != 0:
          path.append(item)
          print(path)
          if find(item, words, seen, target, path):
              return True
          path.pop()

#Takes dictionary file name as input then opens it
#fname = input("Enter dictionary name: ")#dictionary file name
file = open('dictionary.txt')

lines = file.readlines() #each line in file
start = input("Enter start word:") #starting word
words = [] #list of all words of the same length  in dictionary

#iterates of each line in file strips white space off end
for line in lines:
    word = line.rstrip()
    #if anyword same length as start word add to list
    if len(word) == len(start):
      words.append(word)
target = input("Enter target word:") #target word

count = 0
path = [start]#stores the ordered path to target word
seen = {start : True} # dictionary for
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")
