class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 最长回文子串
        n = len(s)
        if n == 1: return s
        max_len = 1
        begin = 0
        dp = [[False]*n for _ in range(n)]
        for j in range(1, n):
            for i in range(j):
                if j-i<3:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j] and j-i+1>max_len:
                    max_len = j-i+1
                    begin = i
        return s[begin:begin+max_len]

if __name__=="__main__":
    lpy = Solution()
    # s = "babad"
    s = "cbbd"
    s = "c"
    print(lpy.longestPalindrome(s))