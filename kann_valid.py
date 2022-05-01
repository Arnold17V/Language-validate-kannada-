import re

def KannOrNot(word):
  rangeStart = ur"\u0C80"
  rangeEnd = ur"\u0CFF"
  pattern = rangeStart + '-' + rangeEnd
    if re.match('^[' + pattern + ']+$',word) != None:
        return True
    else:
        return False

#input
myString = u(input())
wordsList = myString.split()
for eachWord in wordsList:
  if KannOrNot(eachWord):
    prediction() 
  else:
    print("Error! Try to enter only words in the Kannada dialect")
