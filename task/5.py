# 5. Grade calculator in python (if elif else)
number = int(input("Write Your Number:"))
if number >= 80:
    print("A+")
elif number >=70 and number <80:
    print("A")
elif number >=60 and number <70:
    print("A-")
elif number>=50 and number<60:
    print("B")
elif number>=40 and number<50:
    print("C")
elif number>=33 and number<40:
    print("D")
else:
    print("Fail")