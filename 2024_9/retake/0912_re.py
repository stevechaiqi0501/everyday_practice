s = "(())"
stack = []
flag = False
mapping = { 
            ")":"(",
            "}":"{",
            "]":"["
            }

for i in range(len(s)):
    if s[i] in mapping.values():
        stack.append(s[i])
    
    elif s[i] in mapping.keys():
        if not stack or stack.pop() != mapping[s[i]] :
            flag = True
            print(False)
            break
        
if len(stack) != 0:
    print(False)
if not flag:
    print(not False)
    

