class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        first = min(strs, key=len)
        for i in range(len(first)):
            for s in strs:
                if s[i] != first[i]:
                    return first[:i] if i > 0 else ''
        return first
#pythonic solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret
