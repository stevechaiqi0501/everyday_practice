class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] in hashmap.keys():
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        for i in range(len_nums):
            if hashmap[nums[i]] > 1:
                return True
        
        return False

        
#　鳩の巣原理を使った解法
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
#     1. セット（set）の仕組み
# セットは 重複を許さないデータ構造 です。内部的には ハッシュテーブル を利用しており、各要素が一意であることを保証します。

# 主な特徴
# 重複排除: 同じ値を複数回追加しようとしても、1回しか保存されない。
# 順序を保持しない: 要素の順番は保証されない。
# 高速な操作: 検索、追加、削除が平均O(1)の計算量で実行できる。

        