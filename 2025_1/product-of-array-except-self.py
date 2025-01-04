class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = 1
        LtoI = []

        for i in range(len(nums)):

            LtoI[i] =  left
            left = left*LtoI[i]

        right = 1
        RtoI = []

        for i in range(len(nums),0,-1):
            RtoI[i] = right
            right = right*RtoI[i]

        result = []
        
        for i in range(len(nums)):
            result.append(RtoI[i]*LtoI[len(num)-i])

        return result

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = 1
        LtoI = [1] * len(nums)
        RtoI = [1] * len(nums)


        for i in range(len(nums)):

            LtoI[i] =  left
            left = left*nums[i]

        right = 1

        for i in range(len(nums)-1,-1,-1):
            RtoI[i] = right
            right = right*nums[i]

        result = []
        
        for i in range(len(nums)):
            result.append(RtoI[i]*LtoI[i])

        return result

        

        






        
















        