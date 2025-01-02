class Solution:
    def longestCommonPrefix(self, input: list[str]) -> str:
        input_dict = {}
        box = input[0][0]
        ans = ""
        break_line = False
        for i in range(len(input)):
            input_dict[input[i]] = len(input[i])
            
            input_dict.values
            values = list(input_dict.values())

        for i in range(min(values)):
            box = input[0][i]
            for j in range(len(input)):
                 if box == input[j][i]:
                     box = input[j][i]
                 else:
                    break_line = True
                    break
            if break_line:
                break
            
            ans += box
            
        return ans