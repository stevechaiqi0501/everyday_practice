name = str(input("Enter a word: "))

vowels = ["a","e","i","o","u"]

#education 
for i in range(len(name)):
    print("name[",i,"]","->",name[i])
    if name[i] in vowels:
        vowels.pop(name[i])
        
    if vowels is None:
        print("OK")
    
    
        



