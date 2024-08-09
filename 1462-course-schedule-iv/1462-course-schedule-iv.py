class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
        n = numCourses
        graph = [[] for _ in range(n)]
        reversed = [[] for _ in range(n)]
        degree = [0] * n
        
        for i,j in prerequisites:
            graph[i].append(j)
            reversed[j].append(i)
            degree[j] += 1
        
        q = deque([i for i in range(n) if degree[i] == 0])
        sorted = []
        
        while q:
            x = q.popleft()
            sorted.append(x)
            for k in graph[x]:
                degree[k] -= 1
                if(degree[k] == 0):
                    q.append(k)
                    
        pre = [set([i]) for i in range(n)]            
        for s in sorted:
            for k in reversed[s]:
                pre[s].update(pre[k])
        
        print(pre)
        result = []
        for x, y in queries:
            result.append(x in pre[y])
            
        return result
                
        
        
        
                