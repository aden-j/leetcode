class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        jumps = 0
        end = 0
        dist = 0

        for i in range(n - 1):
            dist = max(dist, i + nums[i])

            if i == end:
                jumps += 1
                end = dist

                if end >= n - 1: 
                    break

        return jumps