
#Kadane's algorithm
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = curr_so_far = -float('inf')
        for i in xrange(len(nums)):
            curr_so_far += nums[i] # Add curr number
            curr_so_far = max(curr_so_far, nums[i]) # Check if should abandon accumulated value so far if it's a burden due to negative value accumulated
            max_so_far = max(max_so_far, curr_so_far) # Update answer
            
        return max_so_far
