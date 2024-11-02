vowels = ["a", "e", "i", "o", "u"]
string = "jhgstoyouefgi"
count = 0
for i in range(len(string)): 
    if string[i] in vowels:  
        count +=1
print(count)


