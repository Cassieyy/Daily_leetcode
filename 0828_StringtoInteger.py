class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if not s: return 0
        flag = True
        if s[0] not in ['-','+','0','1','2','3','4','5','6','7','8','9']: return 0
        if s[0]=='-': # 说明是负数
            flag = False
            s = s[1:]
        elif s[0]=="+":
            flag = True
            s = s[1:]
        if not s: return 0
        res = ""
        # if not flag: res+="-"
        if flag==True and s[0] == "-": flag=False
        for tmp in s:
            if tmp.isdigit():
                res += tmp
            else: break
        print
        if not res: return 0
        if not flag: res = int(res)*(-1)
       
        if flag: return min(int(res), 2**31-1)
        else: return max(int(res), -2**31)


if __name__=="__main__":
    lpy = Solution()
    s = "  -123"
    print(lpy.myAtoi(s))