class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two pointers for b-search
        x=0
        y=len(nums)-1
        
        # hack - if less than 5 return min (since it is nto much of computation and handles corner cases)
        if len(nums)<5:
            return min(nums)
        
        # if already sorted, return first number
        if nums[x]<=nums[y]:
            return nums[x]
        
        # binary search to find the point where array is rotated
        while(x<y):
            mid=(x+y)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[x]>nums[mid]:
                y = mid
            else:
                x = mid
