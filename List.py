EX-1 
l1=[1,2,3,"english","mango"]
for i in l1:
   print(i)          o/p- 1 2 3 english mango

EX-2
data = "Hello How are you"
vowels=[]
consonent=[]
vowel="AEIOUaeiou"
for i in data:
    if(i ==' '):
        continue
    elif(i in vowel):
        vowels.append(i)
    else:
        consonent.append(i)
print(vowels)
print(consonent)
