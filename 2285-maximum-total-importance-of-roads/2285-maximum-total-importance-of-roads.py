class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        con = [0] * n
        result = 0
        for i, j in roads:
            con[i] += 1
            con[j] += 1
            
        point = sorted(con)
        
        for i in range(1,n+1):
            result += point[i-1] * i
            
        return result
        
        
        