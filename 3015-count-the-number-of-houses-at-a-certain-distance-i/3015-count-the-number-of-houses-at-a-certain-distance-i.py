class Solution(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        
        result = [0] * n
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if j != i:
                    d = min(abs(i-j), abs(i-x) + 1 + abs(j-y), abs(i-y) + 1 + abs(j-x)) - 1
                    result[d] += 1
                
        return result
        