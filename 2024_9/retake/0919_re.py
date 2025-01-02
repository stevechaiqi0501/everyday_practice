# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

Input = "   fly me   to   the moon  "

list_Input = Input.split(" ")
ans_list = []
for i in range(len(list_Input)):
    if list_Input[i] != '':
        ans_list.append(list_Input[i])
        
print(len(ans_list[-1]))
        
        