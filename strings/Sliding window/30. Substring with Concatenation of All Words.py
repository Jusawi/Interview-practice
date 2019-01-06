class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n, m = len(s), len(words)
        if m == 0:
            return []
        w = len(words[0])
        if w == 0:
            return []
        # create a dictioanry D whose key is strs in 'words' and value is its number
        D = {}
        word_set = set(words)
        for x in word_set:
            num = 0
            # count the number
            for word in words:
                if x == word:
                    num += 1
            D[x] = num
        res = []
        # check every possible index of 's'
        for i in range(0, n-m*w+1, 1):
            if s[i:i+w] in words:   # meet a possible position
                tmp = D.copy() # a shallow copy of 'D'
                j = i+(m-1)*w   # check from tail to head
                while j>=i and tmp.get(s[j:j+w], 0) != 0:
                    tmp[s[j:j+w]] -= 1  # decrease number of the word 
                    j -= w
                if j < i:
                    res.append(i)   # add the index
        
        return res
