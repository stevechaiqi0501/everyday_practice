class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        total_hashmap = {}
        temp_hashmap = {}
        len_strs = len(strs)

        for i in range(len_strs):
            strs_index = strs[i]
            for j in range(len(strs_index)):
                if strs_index[j] in temp_hashmap:
                    temp_hashmap[strs_index[j]] += 1
                else:
                    temp_hashmap[strs_index[j]] = 0

            total_hashmap[strs_index] = temp_hashmap
            temp_hashmap = {}

        temp_total = {}

        for i in range(len_strs):
            if total_hashmap.values(i) in temp_total:
                temp_total[total_hashmap.values(i)].append(total_hashmap.keys(i))
            else:
                temp_total[total_hashmap.values(i)] = [total_hashmap.keys(i)]

        len_temp_total = len(total_hashmap)
        result = []

        for i in range(len_temp_total):
            result.append(temp_total.values(i))
        
        return result







from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 各文字列の構成を保存する辞書
        total_hashmap = {}
        temp_hashmap = {}
        len_strs = len(strs)

        for i in range(len_strs):
            strs_index = strs[i]
            for j in range(len(strs_index)):
                if strs_index[j] in temp_hashmap:
                    temp_hashmap[strs_index[j]] += 1
                else:
                    temp_hashmap[strs_index[j]] = 1  # カウントは1から開始

            # 辞書をタプルに変換してキーとして使用
            total_hashmap[strs_index] = tuple(sorted(temp_hashmap.items()))
            temp_hashmap = {}

        temp_total = {}

        for key, value in total_hashmap.items():
            if value in temp_total:
                temp_total[value].append(key)
            else:
                temp_total[value] = [key]

        result = list(temp_total.values())

        return result

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 各文字列の構成を保存する辞書
        total_hashmap = {}
        temp_hashmap = {}
        len_strs = len(strs)

        for i in range(len_strs):
            strs_index = strs[i]
            for j in range(len(strs_index)):
                if strs_index[j] in temp_hashmap:
                    temp_hashmap[strs_index[j]] += 1
                else:
                    temp_hashmap[strs_index[j]] = 1  # カウントは1から開始

            # 修正①: キーを "i" (添字) にする
            total_hashmap[i] = tuple(sorted(temp_hashmap.items()))
            temp_hashmap = {}

        temp_total = {}

        for key, value in total_hashmap.items():
            # 修正②: key は添字になったので、対応する文字列を取り出す
            original_str = strs[key]
            if value in temp_total:
                temp_total[value].append(original_str)
            else:
                temp_total[value] = [original_str]

        result = list(temp_total.values())
        return result
