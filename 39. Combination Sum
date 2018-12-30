class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        self.combo(res, candidates, target, [], 0)
        return res
    
    def combo(self, res, cand, rem, arr,idx):
        if rem == 0:
            res.append(arr)
        elif rem < 0:
            return
        for i in range (idx, len(cand)):
            self.combo(res, cand, rem - cand[i],arr+[cand[i]], i)
