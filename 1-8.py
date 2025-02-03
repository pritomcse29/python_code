# 1.8 for loop in python and range in python
numbers = [5,10,15,20,25]
sum = 0
for num in numbers:
    print(num)
    sum = sum + num
    if sum > 20:
        print('bigger values')
 
print(sum)

text = "Pagla Howar"
for char in text:
    print(char)

nums = [1,2,3,4,5,6,7,8,9,10]
for c in range(1,10):
    print(c)

friends = ['nobel','ashir','rabi','naz']
for friend in friends:
    print(friend)