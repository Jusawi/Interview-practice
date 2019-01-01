class Solution:
       def __init__(self):
        self.res = []
       
       def subsets(self, nums, path=[]):
           self.res.append(path)
           for i in range(len(nums)):
               self.subsets(nums[i+1:], path+[nums[i]])
           return self.res


class Solution(object):
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
