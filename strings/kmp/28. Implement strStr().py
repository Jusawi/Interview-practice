#KMP ALGORITHM

class Solution:
    def strStr(self, s, x):
        """
        :type s: str
        :type x: str
        :rtype: int
        """
        if not x:
            return 0
        #using kmp to stop backtracking
        j = 0; i = 1;
        lx = len(x)
        
        #creating the lps array
        lps = [0]*lx
        while i < lx:
            while j > 0 and x[i] != x[j]:
                j = lps[j-1]
            if x[i] == x[j]:
                j+=1
            lps[i] = j
            i+=1
            
            
        i,j=0,0
        while i< len(s):
            while j > 0 and s[i] != x[j]:
                j = lps[j-1]
            if s[i] == x[j]:
                j+=1
            if j == lx:
                return i - lx + 1
            i+=1
        return -1
            
