class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        last = n
        for i in range(n-1, 0, -1):
            if i+nums[i-1] >= last: last = i

        return last == 1




        