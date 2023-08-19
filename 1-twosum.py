class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2:
            pass
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sums = nums[i] + nums[j]
                if sums == target:
                    return [i,j] 
