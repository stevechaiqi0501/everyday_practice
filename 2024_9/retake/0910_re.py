roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
         'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

inputRoman = "III"
i = 0
AddedNumber = 0

while i < len(inputRoman):    
    if i + 1 < len(inputRoman) and inputRoman[i:i+2] in roman:
        AddedNumber = AddedNumber + roman[inputRoman[i:i+2]]
        i += 2
        
    else:
        AddedNumber = AddedNumber + roman[inputRoman[i]]
        i += 1

        
print(AddedNumber)

# roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
#          'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

# inputRoman = "CDXLIII"
# i = 0
# AddedNumber = 0
# while i < len(inputRoman):
#     if i + 1 < len(inputRoman) and inputRoman[i:i+2] in roman:
#         AddedNumber = AddedNumber + roman[inputRoman[i:i+2]]
#         i += 2
#     else:
#         AddedNumber = AddedNumber + roman[inputRoman[i]]
#         i += 1
        
# print(AddedNumber)
        
        
    