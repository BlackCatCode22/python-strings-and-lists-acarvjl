# programTwo.py
# 
# Name: Adrian Carvajal
# 
# Date: 8/27/2023
#
# Class: CIT-95
#
#
#
# Starting repo for Python Strings and Lists Program
# String Instructions: ######################################## For this assignment, you will work with various
# string functions to manipulate and analyze text data. You are provided with a sample text string.
# Your task is to write Python code to perform the specified operations using string functions.

# text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
# Length Calculation: Write a function calculate_length(text) that takes the given text as input and returns
# the length of the text (including spaces and punctuation).
# textStr = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."

# Take input from user.
textStr = input("Enter a phrase to evaluate, please: ")


def calStrSize(givenTxt):
    numOfChr = len(givenTxt)
    return numOfChr


# CalStrSize(parameter)

# numOfChr = CarStrSize(argument)

numOfChr = calStrSize(textStr)

print(f"The phrase you entered has a length of: {numOfChr}")
print("\n")
# Uppercase and Lowercase Conversion: Write Python code that takes the given text as input and returns the text in
# uppercase letters followed by the text in lowercase letters.

textStr.lower()
print(textStr)
print("\n")
textStr.upper()
print(textStr)
print("\n")
# Word Count: Write Python code that takes the given text as input and returns the total number of words in the text.
textStr = input("Enter a new phrase, please: ")


def wordCnt(entStr):
    listOfWrd = entStr.split()
    numOfWrds = len(listOfWrd)
    return numOfWrds


totalWrds = wordCnt(textStr)
print(f"The total number of words in the phrase you entered is: {totalWrds}")
print("\n")

# Substring Extraction: Write Python code that takes the given text, and returns the substring of text starting from
# the start index (inclusive) and ending at the end index (exclusive) supplied by a user.

print("Let's take a phrase and extract some strings from it")

# takes input from user
subStrPull = input("Enter some text to work with: ")

# extracting substrings
startIndex = int(input("What index you  wanna start with:? "))
endIndex = int(input("What is the end of the index:? "))

# pulling the indexes start:end
shorterStr = subStrPull[startIndex:endIndex]
print("Substring extracted: ", shorterStr)
print("\n")
# Word Replacement: Write Python code that takes the given text, a target word (input by the user), and replacement
# word (input by the user) as input, and returns the text with all occurrences of the target word replaced by
# the replacement word.

# takes the given text
givenTxt = input("Enter a text: ")
# target word
targetWrd = str(input("Enter the word to replace: "))
# replacement word
rplcemtWrd = str(input("Enter the replacement word: "))

# returns the text with all occurrences of the target word replaced
modifiedTxt = givenTxt.replace(targetWrd, rplcemtWrd)

print("Text with all occurrences of the target word replaced: \n")
print(modifiedTxt )
print("\n")
# Whitespace Removal: Write Python code that takes the given text as input and returns the text with all leading and
# trailing whitespaces removed.

strTxt = " text with all leading and trailing whitespaces removed."
whtSpsRmved = str.rstrip(strTxt)

print(whtSpsRmved)
print("\n")
# Splitting into Sentences: Write a function split_sentences(text) that takes the given text as input and returns a
# list of sentences present in the text.

def sentSplit(txtEnter, delimiter):
    subSentence = txtEnter.split(delimiter)
    return subSentence

txtEnter = "Write a function, split_sentences(text), that take the given text as input."
delimiter = ","
result = sentSplit(txtEnter, delimiter)
print(result)
print("\n")
# Word Reversal: Write Python code that takes the given text as input and returns the text with each word reversed.

revTxtnow = txtEnter[::-1]

print(revTxtnow)
print("\n")

# Character Count: Write Python code that takes the given text and a character as input, and returns the number of
# occurrences of the specified character in the text.

cntStrnew = len(txtEnter)
print(cntStrnew)
print("\n")
# Substring Count: Write Python code that takes the given text and a substring as input, and returns the number of
# occurrences of the specified substring in the text.

txtEnter = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
substring = "o"

cntSubStr = txtEnter.count(substring)
print(f"Substring count of {substring} is: ", cntSubStr)
print("\n")
# Note: You can assume that the input text does not contain any punctuation other than periods.

# Feel free to add or modify your code beyond the minimum requirements. Explore a few new Python programming concepts!
# Test your program code with the provided text:

# text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
#
# List Instructions: ################################################ For this assignment, 
# you will work with the provided string to create a list. You will then apply ten common list 
# operations to manipulate and analyze the list data.
# 
# text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
# list("Python is an amazing programming language. It is versatile, easy to learn, and powerful.")
# ("What is your name!!? ")

# name = input
# def greetAll(name):
print("Hello. What is your name? ")
name = input()
print(f"How do you do {name}?")

print(f"Well, {name}, I am thinking of some string functions to help us learn")

# List Creation: Create a list called word_list by splitting the given text into words.
# word_list = text = 'Python is an amazing programming language. It is versatile, easy to learn, and powerful.'

word_list:  str = input("Let's enter a text to analyze, please!\n")
print("Creating a list called word_List")
print(word_list)
worlList = word_list.split()
print(worlList)

for x in word_list:
    print(x)
#wordList = word_list.split()
print("\n")

# Appending: Append the word "Pythonic" to the word_list.

print("Appending the word \'Pythonic'")

word_list.append('Pythonic')
print(word_list)
print("\n")
# Insertion: Insert the word "awesome" at the beginning of the word_list.

print("Inserting the word \'awesome' at the beginning")

word_list.insert(0, 'awesome')
print(word_list)
print("\n")
# Indexing and Slicing: Print the third word in the word_list and then print a sublist containing the words from the 6th to 9th position.

print("Indexing and Slicing")

newList = word_list[15:17]
print(newList)
print("\n")
subList = word_list[6:9]
print(subList)
print("\n")
# Removal: Remove the word "amazing" from the word_list.

print("Remove the word \'amazing'")
print(word_list)
print("\n")
word_list.remove("amazing")
print(word_list)
print("\n")
# Sorting: Sort the word_list in alphabetical order.

print("Sorting the word_list")
sortWords = word_list.sort()
print(sortWords)

# Counting: Count the occurrences of the word "is" in the word_list.

print("Count the occurrences of the word \'is'")
cntOccurr = word_list.count("is")

print("The occurrence of the word \'is', is: ", cntOccurr)
print("\n")
# Joining: Create a string sentence by joining the words in the word_list with spaces.

print("Creating a join wiht spaces.")

newStrJoin = " ".join(word_list)
print(newStrJoin)
print("\n")
# Reversal: Reverse the order of elements in the word_list.

print("Reverse the order of elements")

print(word_list.reverse())
print("\n")
# Copying: Create a new list copied_list by copying the contents of the word_list.

print("Creating a new list copied_list")
copied_list = word_list.copy()

print(word_list)
print('Copied list: ', copied_list)

# Test each operation thoroughly and print the results for verification.

# Note: Pay attention to the difference between 0-based indexing in lists and the indexing/slicing provided in the assignment.
#Feel free to add or modify your code beyond the minimum requirements. Explore a few new Python programming concepts!
#
#
#
