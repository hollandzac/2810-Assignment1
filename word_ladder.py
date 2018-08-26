#! /usr/bin/env python3
import re
#Computes the length of a list made by
def same(item, target):
 # print([c for (c, t) in zip(item, target) if c == t])
  return len([c for (c, t) in zip(item, target) if c == t])

#This function builds a list by searching the words list and if word
# not in seen or list and the regex search returns true
def build(pattern, words, seen, list):
    #the re search '.' character in pattern matches any character except newline
    #will return true as long as all other characters match plus any letter in the
    # '.' postiion
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

#finds the path to the target word
def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
    print(list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

#Takes dictionary file name as input then opens it
fname = input("Enter dictionary name: ")#dictionary file name
file = open(fname)

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
