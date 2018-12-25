#ref: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
class Solution:
    def nextPermutation(self, nums):
        nidx = len(nums) - 1      

        def reverse(nums, l, r=nidx):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        for i in range(nidx, 0, -1):
            # find longest weakly decreasing (l -> r) suffix
            if nums[i - 1] >= nums[i]: continue
            l, r = i - 1, nidx
            while nums[r] <= nums[l]:
                r -= 1
            # there must be at least 1 successor by defn
            nums[l], nums[r] = nums[r], nums[l]
            reverse(nums, i)
            return
        nums.reverse()
        
        
  #using bisect same logic
  class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = -bisect.bisect_right(nums[i+1:][::-1], nums[i])-1
                nums[i], nums[idx] = nums[idx], nums[i]
                nums[i+1:] = nums[i+1:][::-1]
                return
        nums.reverse()
