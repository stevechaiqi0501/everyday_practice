class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False
        else:
            strS_frequency = {}
            strT_frequency = {}
            for i in range(len_s):
                if s[i] in strS_frequency:
                    strS_frequency[s[i]] += 1
                else:
                    strS_frequency[s[i]] = 0

            for i in range(len_t):
                if t[i] in strT_frequency:
                    strT_frequency[t[i]] += 1
                else:
                    strT_frequency[t[i]] = 0

        if strS_frequency == strT_frequency:
            return True
        else:
            return False

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


from collections import Counter

# 文字列のカウント
s = "anagram"
counter = Counter(s)
print(counter)
# 出力: Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})

# リストのカウント
nums = [1, 2, 2, 3, 3, 3]
counter = Counter(nums)
print(counter)
# 出力: Counter({3: 3, 2: 2, 1: 1})