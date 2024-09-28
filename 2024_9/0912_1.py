s = "}()}"
stack = []
mapping = { 
            ")":"(",
            "}":"{",
            "]":"["
            }

for char in s:
    if char in mapping.values():
        stack.append(char)
        

    elif char in mapping.keys():
        if not stack or mapping[char] != stack.pop():
            print(False)
        
print(not stack)