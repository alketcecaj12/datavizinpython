# define a string
mystring = 'Hi How are you?'

# get the first character
firstchar = mystring[0]
print(firstchar)

# get the last character
lastchar = mystring[-1]
print(lastchar)

# get the first word
firstword = mystring.split(' ')[0]
print(firstword)

# declare a set in Python
thisset = {"apple", "banana", "cherry"}
print(thisset)

#another way to declare a set in Python
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# add element to set
thisset = set(("apple", "banana", "cherry"))
thisset.add("damson")
print(thisset)

# remove element to set
thisset = set(("apple", "banana", "cherry"))
thisset.remove("banana")
print(thisset)

#get the number of items in set
thisset = set(("apple", "banana", "cherry"))
print(len(thisset))


# lists in Python - using the list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# using append() to add elements to a list
thislist = list(("apple", "banana", "cherry"))
thislist.append("damson")
print(thislist)

# using remove method to remove elements to a list
thislist = list(("apple", "banana", "cherry"))
thislist.remove("banana")
print(thislist)

# find the length of a list with len() method
thislist = list(("apple", "banana", "cherry"))
print(len(thislist))


# length of a tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))