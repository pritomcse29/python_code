# 2.3 (advanced) kargs, multiple return from a function
def full_name(first, last):
    name = f'full name is: {first} {last}'
    return name
#take parameter in order (serial wise)
# name = full_name('Alu', 'Kodu')

#serial oize na hoileo cholbe
name = full_name(last="kodu" , first="alu")
print(name)

#def famous(**kargs) key with value **addition recieved data as dictionary
def famous_name(first, last,title,**addition):
    name = f'{first} {last} {title}'
    # print(addition['title'])
    for key,value in addition.items():
        print(key,":",value)
    return name
    
name = famous_name(first='Pritom', last='Sarkar', title='Engineer',addition="Fat")
print(name)

