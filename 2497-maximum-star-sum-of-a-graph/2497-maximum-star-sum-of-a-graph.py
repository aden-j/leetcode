class Solution(object):
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        n = len(vals)
        graph = [[] for _ in range(n)]
        
        for u,v in edges:
            if vals[v] > 0:
                graph[u].append(vals[v])
            if vals[u] > 0:
                graph[v].append(vals[u])
            
        result = float('-inf')
        for i in range(n):
            list = graph[i]
            list.sort(reverse = True)
            s = 0
            if (len(list) >= k):
                s = sum(list[:k])
            else:
                s = sum(list)
            result = max(result, s + vals[i])
                
        return result
        