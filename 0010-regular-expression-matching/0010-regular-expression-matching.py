class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        n = len(s)
        m = len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True
        for j in range(1, m + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    if p[j-2] == ".":
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] == s[i-1])
                else:
                    if s[i-1] == p[j-1]: 
                        dp[i][j] = dp[i-1][j-1]

        return dp[n][m]

        
        