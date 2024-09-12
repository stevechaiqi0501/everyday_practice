roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
         'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

inputRoman = "CDXLIII"
output_ans = 0
i = 0

while i < len(inputRoman):
    if i + 1 < len(inputRoman) and inputRoman[i:i+2] in roman:
        output_ans += roman[inputRoman[i:i+2]]
        i += 2
    else:
        output_ans += roman[inputRoman[i]]
        i += 1
        
print(output_ans)
        
# roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
#          'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

# inputRoman = "CDXLIII"
# output_ans = 0
# i = 0

# while i < len(inputRoman):
#     # Check if the next two characters form a valid numeral
#     if i + 1 < len(inputRoman) and inputRoman[i:i+2] in roman:
#         output_ans += roman[inputRoman[i:i+2]]
#         i += 2
#     else:
#         # Check for the single character
#         output_ans += roman[inputRoman[i]]
#         i += 1

# print(output_ans)
