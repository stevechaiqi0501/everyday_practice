strs = ["flower","flow","flight"]

first = strs[0]
last = strs[-1]
output_str = ""
i = 0
while i < len(first) and i < len(last):
    if first[i] == last[i]:
        output_str += first[i]
    else:
        break
    
print(output_str)