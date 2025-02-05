# 2.4 local and global scope in python
balance = 3000
def buy_things(item,price):
    # local scope variable
    # you can access global vaiable without using the global keyword
    dream_phone = 'xphone'
    global balance # global balance
    balance = balance - price 
    print(f'{dream_phone} after buying balance {item}' , balance)

buy_things('sunglass',1000)

