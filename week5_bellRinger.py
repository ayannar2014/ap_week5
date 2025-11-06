# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.

# magic = 'abracadabra'
# fifth_char = print (magic [4])
# second_to_last_char = print (magic[-2])
# first_c_index = print(magic.index('c'))
# # find the first occurrence of letter 'c'...first time it appears is four 
# last_a_index = print(magic.rindex('a'))
# # find the last occurrence of the letter 'a'...the r in "rindex" stahds for reverse 

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.

# alphabet = 'abcdefghijklmonopqrstuvwxyz'
# hij = print (alphabet.index('hij'))
# hij2 = print (alphabet[7:10])
# m_index = print(alphabet.index('m'))
# every_second = print (alphabet[0:13:2])
# reversed_alphabet = print(alphabet[0: :-1])

# dream_speech = 'When we allow freedom to ring—when we let it ring from every city and every hamlet, from every state and every city, we will be able to speed up that day when all of Gods children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual, Free at last, Free at last, Great God a-mighty, We are free at last.'
# reversed_alphabet = print(dream_speech[: :-1])


# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
# famous_quote = 'Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy'
# john_f_kennedy = print(famous_quote.find("John F. Kennedy"))
# extracted_name = print(famous_quote[83: ])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
# info= 'Python is fun. Fun is good. Good is subjective.'
# subjective = print(info.find("subjective"))
# This will find the word subjective which was at output: 36
# extracted_name = print (info[36: ])
#  b. Extract every third word.
# third_letter = print(info[::3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
# words = info.split()
#split the string words 
# print(words)
#it will print ['Python', 'is', 'fun.', 'Fun', 'is', 'good.', 'Good', 'is', 'subjective.']
# reversed_words = ' '.join(reversed(words))
# print(reversed_words)


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
# text= "MAY THE FORCE BE WITH YOU" 
# print(text.lower())
# print(text.upper())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],

# motto= ["Make", "haste", "slowly."]

# a. Convert the list into a single string.
# joined_motto = ' '.join(motto)
# print(joined_motto) 
# b. Now, split the string at every occurrence of the letter 'a'.
# joined_motto_split = joined_motto.split('a')
# print(joined_motto_split) 
#output makes ['M', 'ke h', 'ste slowly.']

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# sentence ="Life is what happens when you are busy making other plans."
# replaced_sentence = print(sentence.replace("busy", "distracted").replace("plans", "mistakes"))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
# repeated_word = print("Iteration "* 7)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

word= "moonlight"
quote= "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

word_in_quote = print( word in quote)
#output is false

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.