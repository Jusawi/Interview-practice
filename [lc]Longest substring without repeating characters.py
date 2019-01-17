def lengthOfLongestSubstring(self, s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            # update the res
            res = max(res, i-start)
            # here should be careful, like "abba"
            start = max(start, dic[ch]+1)
        dic[ch] = i
    # return should consider the last 
    # non-repeated substring
    return max(res, len(s)-start)


#SLIDING WINDOW APPROACH -- LESS EFICIENT

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, start, end, counter = 0, 0, 0, 0
        char_dict = collections.defaultdict(int)
        while end < len(s):
            if char_dict[s[end]] > 0:
                counter += 1
            char_dict[s[end]] += 1
            end += 1
            while counter > 0:
                char_dict[s[start]] -= 1
                if char_dict[s[start]] > 0:
                    counter -= 1
                start += 1

            max_len = max(max_len, end-start)
        
        return max_len
