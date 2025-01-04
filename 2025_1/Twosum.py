class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        hashmap = {}

        for i in range(len_nums):
            hashmap[nums[i]] = i

        for i in range(len_nums):

            sub_value = target - nums[i]         
            if sub_value in nums and hashmap[nums[i]] != i:
                return [i,hashmap[target]]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        hashmap = {}

        for i in range(len_nums):
            hashmap[nums[i]] = i

        for i in range(len_nums):

            sub_value = target - nums[i]
            # "引いた値"がiとは異なるインデックスであることを確認するのだからhashmap[sub_value]じゃないとあかんやろ
            if sub_value in nums and hashmap[nums[i]] != i:
            # ほんでリターーんもsub_valueがindexならなあかんやろ
                return [i,hashmap[target]]
            
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        hashmap = {}

        for i in range(len_nums):
            hashmap[nums[i]] = i

        for i in range(len_nums):

            sub_value = target - nums[i]
            if sub_value in hashmap.keys() and hashmap[sub_value] != i:
                return [i,hashmap[sub_value]]


