class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        
        for i, j in roads:
            graph[i].append(j)
            graph[j].append(i)
            
        result = 0
        def dfs(start, parent):
            res = 0
            rep = 1
            
            for x in graph[start]:
                if x != parent:
                    r, p = dfs(x, start)
                    res += r
                    rep += p
            
            if start != 0:
                res += (rep / seats) + (1 if (rep % seats > 0) else 0)
            
            return res, rep
        
        return dfs(0, -1)[0]