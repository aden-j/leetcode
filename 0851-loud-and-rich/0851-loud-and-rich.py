class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        
        n = len(quiet)
        graph = [[] for _ in range(n)]
        
        for a,b in richer:
            graph[b].append(a)
            
        result = [-1] * n
        
        def cal(start):
            if result[start] != -1:
                return result[start]
            m = start
            for x in graph[start]:
                if quiet[m] > quiet[cal(x)]:
                    m = cal(x)
                
            result[start] = m
            return m
        
        for i in range(n):
            cal(i)
            
        return result