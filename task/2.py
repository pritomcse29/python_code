"""
2. take 3 numbers from the user and give me the largest number as output
"""
num1 = int(input("Write Num1:"))
num2 = int(input("Write Num2:"))
num3 = int(input("Write Num3: "))
if num1>num2 and num1>num3:
    print(num1," "+"is largest number")
elif num2>num1 and num2>num3:
    print(num2," "+"is largest number")
else:
    print(num3," "+"is largest number") 

