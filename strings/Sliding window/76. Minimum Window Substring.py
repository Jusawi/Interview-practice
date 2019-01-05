#Simple Answer(General idea)
class Solution:
    def minWindow(self, s, t):
        count=0
        size=len(s)
        end,start=0,0
        m=collections.defaultdict(int)
        for i in t:
            if i not in m:
                count+=1
            m[i]+=1
        anslen=size
        ans=""
        for end in range(size):
            if s[end] not in m:
                continue
            m[s[end]]-=1
            if m[s[end]] == 0:
                count-=1
            
            while count == 0:
                if end-start<anslen:
                    anslen = end-start
                    ans=s[start:end+1]
                startc=s[start]
                start+=1
                if startc not in m:
                    continue
                m[startc]+=1
                if m[startc] == 1:
                    count+=1
                    break
        #if anslen == size+1:
          #  return ""
        return ans
        
#### More EFficient Solution
from collections import defaultdict
class Solution:
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        freq_list = defaultdict(int)
        char_num = len(set(T))

        for c in T:
            freq_list[c] += 1

        cur_start = 0
        min_pos = [float('-inf'), float('inf')]

        for idx, cur_c in enumerate(S):
            freq_list[cur_c] -= 1
            if freq_list[cur_c] == 0:
                char_num -= 1

            if char_num == 0:
                while cur_start <= idx and char_num == 0:
                    freq_list[S[cur_start]] += 1
                    if freq_list[S[cur_start]] == 1:
                        char_num += 1
                    cur_start += 1

                if idx - cur_start + 1 < min_pos[1] - min_pos[0]:
                    min_pos = [cur_start-1, idx]

        if min_pos[0] == float('-inf'):
            return ''
        else:
            return S[min_pos[0]:min_pos[1]+1]
