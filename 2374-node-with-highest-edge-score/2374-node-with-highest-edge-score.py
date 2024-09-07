class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        
        n = len(edges)
        
        v = [0] * n
        result, value = (0, 0)
        
        for i in range(n):
            v[edges[i]] += i
            if v[edges[i]] > value:
                result = edges[i]
                value = v[edges[i]]
            elif v[edges[i]] == value:
                result = min(edges[i], result)
        
        return result