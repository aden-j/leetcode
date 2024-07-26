class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = []
        n = len(graph)
        
        q = deque([(0, [0])])
        while q:
            x, list = q.pop()
            for i in graph[x]:
                l = list + [i]
                if i == n-1:
                    result.append(l)
                else:
                    q.append((i, l))
                           
                           
        return result