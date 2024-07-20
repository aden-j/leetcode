class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        positive_inf = float('inf')
        dist = [[] for _ in range(n+1)]
    
        least = [positive_inf] * (n+1)
        least[k] = 0
        
        for time in times:
            dist[time[0]].append((time[1],time[2]))
            
        q = deque([k])
        
        while q:
            x = q.popleft()
            for v,w in dist[x]:
                if least[x] + w < least[v]:
                    q.append(v)
                    least[v] = least[x] + w
        
        result = max(least[1:])
            
        if result == positive_inf:
            return -1
        return result
        
            
        