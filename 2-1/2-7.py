# 2.7 list methods in python
numbers = [12,45,98,68]
numbers.append(56) # add the element in the last position in list
print(numbers)
numbers.insert(2,71)
print(numbers)
if 8 in numbers:
   numbers.remove(98)
print(numbers)

last = numbers.pop()

index = numbers.index(45)

sorted = numbers.sort()
numbers.reverse()






