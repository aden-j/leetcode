class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        
        n = len(edges)
        
        def dist(start):
            d = [-1] * n
            node = start
            dist = 0
            while node != -1 and d[node] == -1:
                d[node] = dist
                node = edges[node]
                dist += 1
            return d

        d1 = dist(node1)
        d2 = dist(node2)

        least = float('inf')
        result = -1

        for i in range(len(edges)):
            if d1[i] != -1 and d2[i] != -1:
                m = max(d1[i], d2[i])
                if m < least:
                    least = m
                    result = i
                elif m == least and i < result:
                    result = i

        return result
            