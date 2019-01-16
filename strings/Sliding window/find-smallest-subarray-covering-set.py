#start from the smallest array and move up to satisfy condiition
#after fining the first range trim the left side 
#repeat the process again and again and update res
import collections
astr = ["apple", "banana", "apple", "apple", "dog", "cat", "apple", "dog", "banana",
"apple", "cat", "dog"]
search = ["banana","cat"]

count = collections.Counter(search)
res = (-1, -1) #final answer for this question is (8, 10)
start = 0
missing = len(search)
for end,p in enumerate(astr):
    if p in count and count[p] == 1:
        count[p]-=1
        missing -=1
    while missing == 0:
        if res == (-1,-1) or (res[1] - res[0] > end - start):
            res = (start, end)
        temp = astr[start]
        start+=1
        if temp in count:
            count[temp]+=1
            missing+=1
print(res)
