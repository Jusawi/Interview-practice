class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq 
        heapq.heapify(nums) 
        return heapq.nlargest(k, nums)[-1]
