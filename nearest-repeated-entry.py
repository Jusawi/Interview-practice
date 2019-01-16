import collections
s = "all work and no play makes for no work no fun and no results"
s = s.split()
mini = l = len(s)
dic = collections.defaultdict()
for i, n in enumerate(s):
    if n in dic:
        mini = min(i-dic[n], mini)
    dic[n] = i
print (mini)
