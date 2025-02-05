# 3.1 String Immutable and string methods
name1 ='Pritom Sarkar'  
name2 = "Joti\'s Sarkar"
name3 = """
   Sakib Khan
   number one
"""
# print(name1)


"""
 We can use escape
 Multiline String
 String is a sequence of characters
 Mutable means changeable
 immutable means you can not change it
 name[0] = 'R'
"""

# for char in name2:
#     print(char)

print(name2[3])

print(name2[1:6])
print(name2[-3])
print(name2[::-1])


if 'Joti' in name2:
    print('exists')
print(name2.upper())
print(name2.lower())