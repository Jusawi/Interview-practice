class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s2:
            return True
        l, r = 0, len(s1)
        cnt1 = collections.Counter(s1)
        cnt2 = collections.Counter(s2[l:r]) #creating a window
        if cnt1 == cnt2:
            return True
        
        while (r< len(s2)):
            cnt2[s2[r]] += 1
            cnt2[s2[l]] -= 1
            if not cnt2[s2[l]]: del cnt2[s2[l]] 
            l+=1
            r+=1
            if cnt1 == cnt2:
                return True
        if cnt1 == cnt2:
                return True
        return False
