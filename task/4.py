# run a loop and show my the odd numbers between 39 to 68
for e in range(39, 69):
    if e % 2 == 1:
        print(e)

sum = 0
for e in range(39,69):
    if e%2==1:
        sum = sum + e
print("Sum: ",sum) 