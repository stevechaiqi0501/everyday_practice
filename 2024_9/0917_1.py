haystack = str(input())
needle = str(input())

for i in range(len(haystack) - len(needle) + 1):
    if haystack[i:i+len(needle)+1] == needle:
        print(i)
    