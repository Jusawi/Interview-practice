 class Solution:
        # @param {string} s
        # @return {boolean}
        def isValid(self, s):
            stack=[]
            for i in s:
                if i in ['(','[','{']:
                    stack.append(i)
                else:
                    if not stack or {')':'(',']':'[','}':'{'}[i]!=stack[-1]:
                        return False
                    stack.pop()
            return not stack
            

#Intuitive method to impress others
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False
