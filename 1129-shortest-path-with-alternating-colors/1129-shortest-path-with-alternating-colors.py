class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        
        r_graph = [[] for _ in range(n)]
        b_graph = [[] for _ in range(n)]
        
        for x,y in redEdges:
            r_graph[x].append(y)
            
        for x, y in blueEdges:
            b_graph[x].append(y)
            
        b_result = [-1] * n
        r_result = [-1] * n
        
        q = deque([(0,0,'r'),(0,0,'b')])
        while q:
            dist, node, path = q.popleft()
            if path == 'r':
                if r_result[node] == -1:
                    r_result[node] = dist
                    for x in b_graph[node]:
                        q.append((dist+1, x, 'b'))
            else:
                if b_result[node] == -1:
                    b_result[node] = dist
                    for x in r_graph[node]:
                        q.append((dist+1, x, 'r'))
                        
        return [
            min(r, b) if r != -1 and b != -1 else max(r, b) 
            for r, b in zip(r_result, b_result)
        ]