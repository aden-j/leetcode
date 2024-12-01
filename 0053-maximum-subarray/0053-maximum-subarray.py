class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = nums[0]
        current = 0
        
        n = len(nums)
        
        for n in nums:
            current += n
            res = max(current, res)
            if current < 0:
                current = 0
            
        return res
        