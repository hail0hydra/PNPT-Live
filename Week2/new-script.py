#!/usr/bin/python3


#IMPORTING MODULES - Importing is important.
import sys #system functions and parameters
from datetime import datetime as dt

# argv = $1
# sys.exit()

# print(sys.version) #version of python
# print(dt.now())



# ADVANCED STRINGS

my_name = "Hail Hydra"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4])


print(sentence.split()) # takes a delimeter - default is space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split) # takes delimeter as well
print(sentence_join)
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                       hello        "
print(too_much_space.strip())

print("A" in "Apple") # returns True
print("a" in "Apple") # returns False

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())


movie = "The Hangover"
print("My favourite movie is {}.".format(movie))



def nl():
    print("\n")


nl()


# DICTIONARIES - Key/Value Pairs {}

drinks = {"White Russian" : 7, "Old Fashion": 10, "Lemon Drop" : 8} # drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob","Linda","Tina"], "IT": ["Gene","Louise","Teddy"], "HR":["Jimmy Jr.","Mort"]}
nl()
print(employees)

employees["Legal"] = ["Mr. Frond"] # Add new key/value pair
print(employees)

employees.update({"Sales": ["Andie","Ollie"]}) # add new key/value pair - appended to end
print(employees)


drinks['White Russian'] = 8

print(drinks)

print(drinks.get("White Russian")) # returns value of key
