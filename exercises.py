'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python.
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening.


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15
#25
8 - 1
# 7
10 * 2
# 20
35 / 5
# 7

35 / 4
# 8.75
35 // 4
# 8
# What is the difference between the / operator and the // operator?
# The / operator results in a floating point, which means it results in a decimal. The // operator is int division and results in an int, something that does not have a decimal.

2 ** 5
#32
# What does the ** operator do?
# It is a power operator. In this case, 2 to the fifth power.
5 % 3
# 2
5 % 2
# 1
5 % 4
# 1
# What does the % operator do?
# It finds the remainder.

(1 + 3) * 2
# 8
# What effect do the parenthesis have on this statement?
# The program follows order of operations, meaning that operators in the parenthesis will be done first.

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
# <class 'int'>
type(3.0)
# <class 'float'>
type("word")
# <class 'str'>
type(True)
# <class 'boolean'>
type(False)
# <class 'boolean'>
type(None)
# <class 'None'>
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another.
int(3.0)
# 3
float(7)
# 7.0
str(55)
# '55'
bool(1)
# True
# How can you tell the difference between these four different types?
# int is a number that has no decimal. Floats are numbers with a decimal point. Strings are a series of characters, within quotes. A boolean is a true or false.

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
# It concatenates the string.

"This is a string"[0]
# 'T'
"This is a string"[5]
# 'i'
"This is a string"[8]
# 'a'
# What is happening as you change the number?
# As you change the number, the position changes, and so it returns a different character.

"This is a string"[-1]
# 'g'
# What happens when you use a negative number?
# It starts from the back; thus, [-1] returns the last character.

"%s can be %s" % ("strings", "interpolated")
# What is happening here?
#The first %s is replaced by the first object in the brackets and the second is replaced by the second.

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
#'strings can be formatted'

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
#'Bob wants to eat lasagna'

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
# "Hello, Tanner"
# What just happened?
#  input takes a response from the user.

# For your next assignment, you will need to use random numbers
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
# It is creating a random float from zero to one.

randint(1,100)
# How is this different?
# This creates a random integer from 1 to 100. (Integers do not have decimals.)

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# The items were rearranged.

print(sample(items, 1))
# What does this do?
# This selects an item at random from the brackets.

print(sample(items, 5))
# What does the second parameter control?
# The second parameter determines how many items to return.

for i in range(0,5):
	print(i)
# For each of the ints in the range, the program runs through. The first number is inclusive, and the second is not.
# What is happening here? What happens if you change the two range parameters?
# It will increase or decrease the amount of times it runs through.
