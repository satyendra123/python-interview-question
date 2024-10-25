#EX-1 
anpr = {'a':5,'b':6,'c':7}
print(anpr['a'])

#EX-2
anpr = {'a':5,'b':6,'c':7}
c= anpr['a']+anpr['b']+anpr['c']
print(c)

#EX-3 include other keys and values
anpr = {'a': 5, 'b': 6, 'c': 7}
anpr['d'] = 10 
print(anpr)

#EX-4 del and pop method 
# Use del when you want to remove a key without needing its value.
anpr = {'a': 5, 'b': 6, 'c': 7, 'd': 10}
del anpr['c']
print(anpr)

#using pop() method
#Use pop() when you want to remove a key and also need the value that was associated with it.
anpr = {'a': 5, 'b': 6, 'c': 7, 'd': 10}
anpr.pop('c')
print(anpr)

# man lo ki mujhe programm me ek empty dictionary banana hai aur usme jo data aayenge usko return krna hai
#EX-1 
a= dict();
a['c']=5;
a['d']=6;
a['e']=7;
print(a)

#EX-2 
a={};
a['c']=5;
a['d']=6;
a['e']=7;
print(a)

#EX-3 
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = {'even': [], 'odd': []}

for i in data:
    if i % 2 == 0:
        number['even'].append(i)
    else:
        number['odd'].append(i)
        
print("Even numbers:", number['even'])
print("Odd numbers:", number['odd'])

#EX-4
a = ["satyendra", "satyam", "kalika"]
b = [150, 140, 160]
b = sorted(b)

data = {}
for i in range(len(a)):
    data[a[i]] = b[i]
print(data)


