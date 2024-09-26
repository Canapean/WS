    #здание 1
#phrase ="мне так нарвится готовыть. Занимался бы этим каждый день!"
#phrase = phrase.replace("!","").replace(".","").split(' ')
#print(phrase)

    #здание 2
#a = int(input('введите число'))
#if a==2:
#    print("2")
#elif a==5:
#    print("2")
#elif a==8:
#    print("2")
#elif a==12:
#    print("2")
#else:
#    print(a)

    #здание 3
#x = 2
#y = 4
#output = "x" if x**2 > y*2 else "y"
#print(output)

    #здание 4
#a =[1,2,3,4,5,6,7,8,9,10]
#a=a[1::2]
#print(a)

    #здание 5
#a = [1,2,3,4,5,6,7,8,9,10]
#a.append('52')
#print(a)
#a.pop(0)
#print(a)
#a.remove(7)
#print(a)
#print(a.index('52'))

    #здание 6
#a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
#out = 0
#for i in a:
#    out += i
#print(out)

    #здание7
#import random
#symb = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#a =[]
#for i in range(100000):
#    stoke = ''
#    for i in range(3):
#        stoke += random.choice(symb)
#    a.append(stoke)
#t =[]
#for r in a:
#    if r not in t:
#        t.append(r)
#print(t)
#print(len(t))

#import string 
#abc = string.ascii_lowercase
#base_string = input("Введите строку: ")
#secret = ""
#for symbol in base_string:
#    index = abc.index(symbol)
#    if index < 23:
#        new_index = index + 3
#        new_symbol = abc[new_index]
#        secret += new_symbol
#    elif index == 23:
#        new_index = 0
#        new_symbol = abc[new_index]
#        secret += new_symbol
#    elif index == 24:
#        new_index = 1
#        new_symbol = abc[new_index]
#        secret += new_symbol
#    elif index == 25:
#        new_index = 2
#        new_symbol = abc[new_index]
#        secret += new_symbol
#print(secret)

d = {
    'Алабуга это - ...?':"возможности",
    "Любимый цвет?":"black"
}
count = 0

answer = d.keys()
for a in answer:
    print(a)
    b=input()


















