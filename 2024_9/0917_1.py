haystack = str(input()) #leetcode
needle = str(input()) #leeto

for i in range(len(haystack)-len(needle)):
    if haystack[i:i+len(needle)+1] == needle:
        print(i)