class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s= s.strip()
        if len(s) == 0:
            return 0
        sign = 1
        if s[0] == '-' or s[0] == '+':
            sign= [1,-1][0 if s[0] == '+' else 1 ]
            s=s[1::]
        for i in range(len(s)):
            if (s[i].isdigit()):
                i = i
                
            else:
                s = s[:i]
                break
        if len(s) == 0:
            return 0
        return max(-2147483648,min(sign*int(s), 2147483647))
