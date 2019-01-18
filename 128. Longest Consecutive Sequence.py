#Naive approach O(nlongn) complexity
arr = [4,10,5,3,1,6,100]
res= 1
arr.sort() 
cures = 1

for i in range (1,len(arr)):
    if arr[i-1]+1 == arr[i]:
        cures += 1
    else:
        res = max(res , cures)
        cures = 1
print(res)

#Leetcode solution
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        num_set = set(nums)
        longest = 1
        for num in num_set:
            if num - 1 not in num_set: #For finding the smallest element of the range possible
                current = num
                consec = 1
                while current + 1 in num_set:
                    current += 1
                    consec += 1
                    longest = max(consec, longest)
        return longest

#EPI Solution - Most effiecient
def longest_contained_range(A):
    # unprocessed_entries records the existence of each entry in A.
    unprocessed_entries = set(A)

    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()

        # Finds the lower bound of the largest range containing a.
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        # Finds the upper bound of the largest range containing a.
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        max_interval_size = max(max_interval_size,
                                upper_bound - lower_bound - 1)
    return max_interval_size
    
