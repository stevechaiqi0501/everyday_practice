# prctice for twosum

class Solutions:
    def TwoSum(self,nums:list[int],target:int)-> list[int]:
        
        temp_TargetDict = {}
        
        for i in range(len(nums)):
            temp_TargetDict[nums[i]] = i
            
        for i in nums:
            temp_sub = target - nums[i]
            if  temp_sub in nums and temp_TargetDict[temp_sub] != nums[i]:
                return [temp_TargetDict[nums[i]],i]
            else:
                return[]
            

    

    