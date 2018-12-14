class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = collections.defaultdict(int)
        for n in nums:
            d[n] += 1
        res = []
        if 0 in nums and d[0] >= 3:
            res += [0,0,0],
        pos = []
        neg = []
        for k in d:
            if k>0 :
                pos += k,
            else:
                neg += k,
        for p in pos:
            for n in neg:
                t = -(p+n)
                if t in d:
                    if t < n:
                        res += [t, n, p],
                    elif t > p:
                        res += [n, p, t],
                    elif t in (p,n) and d[t] > 1:
                        res += [n, t, p],
        return res
