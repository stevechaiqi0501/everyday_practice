s = "}()}"
stack = []
mapping = { 
            ")":"(",
            "}":"{",
            "]":"["
            }
for i in range(len(s)):
    if s[i] in mapping.values():
        stack.append(s[i])
    elif not stack or mapping[s[i]] != stack.pop():
        print(False)
        