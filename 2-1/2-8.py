# 2.8 (advanced) list comprehension in python
numbers = [45,87,96,65,43,90,85,14,26,61,70]
odd=[]
# for num in numbers:
#     if num % 2 == 1 and num % 5 ==0:
#         odd.append(num)
# print(odd) 

# odd_nums = [num for num in numbers if num % 2==1]
odd_nums = [num for num in numbers if num % 2==1 if num%5 ==0]
print(odd_nums)

players =['pritom','sakib','liton']
age = [38,37,32]
age_comb = []
for player in players:
    # print('player: ',player)
    for ages in age:
        # print(player,age)
        age_comb.append([player,age])
print(age_comb)
age_comb2 = [[player,ages] for player in players for ages in age]
print(age_comb2)