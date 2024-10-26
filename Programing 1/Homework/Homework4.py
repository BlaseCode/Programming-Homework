"""
Homework 4: Programming 1 - COP2220

File by: Kyle Francis
"""

"""
Exercise 1: Digital Library System:

You are tasked with creating a simple digital library system where users can manage a collection of
books. The system will use dictionaries to store book details and sets to keep track of book categories.

"""

from time import sleep

#Part 1: Managing Books with a Dictionary


#Create an empty dictionary to store the keys and the values given
library = {} 

#Create an empty list to update the info in the dictionary later on in the assignment
updated_info = {}

#(a) Add a book to the library by asking for the title and author
title = input("Please enter the title of the book: \n").capitalize()

author = input("Please enter the name of the author: \n").capitalize()


#pass the inputs entered by the user into the dictionary by associating the keys to the values:
library[title] = author #[title] ==> stores the key to be searched and "author" is its value. 

#(b) Retrieve author of a book using its title (.get()) to handle cases where the book isn’t found).
#look for the book given in the first position and return "This book is not inside the library"
sleep(1)
failed_lookup = library.get("The Adventures of Tom Sawyer", "This book is not inside the library\n") #outputs this book is not in the library


 #prints the failed output
print(f"{failed_lookup}")


#(c) Update the author of a book if it already exists in the library (research about the .update() method and use it).
sleep(2)
print("This is to test out the update method: \n")


#Get the "Title" & "Author" names that's needed to update the dictionary
chosen_title = input("Please enter the title that you wish to change: \n").capitalize()

update_author = input("Please enter the authors name that you would like to put: \n").capitalize()

#put the names into an empty list to that stores the updated info:
updated_info[chosen_title] = update_author #stores the input of the author into the searched title

#update the dictionary
library.update(updated_info) #updates the dictionary, if not updated the book title is stored in the dictinary and the author is assigned

#show the "Title" & "Author" that we have so far
sleep(2)
print(f"This is the now updated library: {library}")

#(d) Remove a book from the library using its title (use .pop()).
#Get the input of the title that the user wants to remove:
sleep(1)
remove_title = input("Please enter the title of the book that you want deleted from the library: \n")

#remove the title given from the dictionary:
library.pop(remove_title)

#print the library that was stored:
print(f"{library.items()}")


