EX-1 
l1=[1,2,3,"english","mango"]
for i in l1:
   print(i)          o/p- 1 2 3 english mango

EX-2 counting the total vowels and consonent     EX-3                                          
data = "Hello How are you"                       data = "Hello How are you"
vowels=[]                                        capitalize_word=[]
consonent=[]                                     words= data.split(' ')
vowel="AEIOUaeiou"                               for word in words:
for i in data:                                       capitalize = word[0].upper() + word[1:]
    if(i ==' '):                                     capitalize_word.append(capitalize)
        continue                                  result=''
    elif(i in vowel):                             for word in capitalize_word:   
        vowels.append(i)                              result+= word+' '
    else:                                          print(result)
        consonent.append(i)
print(vowels)
print(consonent)

