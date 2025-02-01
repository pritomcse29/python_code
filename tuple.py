t = ("orange","orange","apple","banana","grape") # tuple allow duplicate value
print(t)
# len()
print(len(t))

#Create Tuple With One Item
t2 = ("apple")
t3 = ("apple",)
print(type(t2)) #<class 'str'>
print(type(t3)) #<class 'tuple'>

# Tuple Items - Data Types
# Tuple items can be of any data type:
# Example String, int and boolean data types:

t4 = ("a","b","c")
t5 = (1,2,3)
t6 = (True, False)

print(t4)
print(t5)
print(t6)

t7 = ("a",1,True)
print(t7)
print(type(t7))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print(thistuple[0])
print(thistuple[-1])
# Negative Indexing
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc. 

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
# print(thistuple[:3]) # 0 - (3-1 =2)
# print(thistuple[2:3]) # first one is start position of an tuple and 2nd is lastPosition - 1

#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

# Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
tup = ("Apple","Banana","Orange","Grape")
if "Apple" in tup:
    print("Apple is in tuple")
