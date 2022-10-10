class Solution(object):
    def twoSum(self, nums, target):
        s=set()
        for i in range(len(nums)):
            
            if (target-nums[i]) in s:
                return (i,nums.index(target-nums[i]))
            s.add(nums[i])
        
