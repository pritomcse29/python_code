# 2.2 Default parameters and args in python
def sum(num1, num2, num3=0, num4=0, num5=0):
    result = num1 + num2 + num3
    return result
total = sum(99 , 11 ,5)
print('total: ',total)

#arg
# *parameter diye multiple sonkhok parameter pass korte parbo
def all_sum(*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(sum)
        sum = sum + num
    return sum
total = all_sum(45, 46,89,11,81,5,2,77)
print('all sum: ', total)