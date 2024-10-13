class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        
        graph = [[] for _ in range(n)]
        for x,y in invocations:
            graph[x].append(y)
            
        inv = set()
        q = deque([k])
        
        while q:
            x = q.popleft()
            if x not in inv:
                inv.add(x)
                for i in graph[x]:
                    if i not in inv:
                        q.append(i)
        
        result = [i for i in range(n)]
        for x, y in invocations:
            if x not in inv and y in inv:
                return result
        
        return [x for x in result if x not in inv]
            
        