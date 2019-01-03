##Standard Algorithm for LPS Array caliculation - Refer KMP Algorithm
#Editorial
class Solution:
	# @param A : string
	# @return an integer
	def calc_LPS_Array(self, P):
	    #Standard Algorithm for LPS Array caliculation - Refer KMP Algorithm
	    m = len(P)
	    lps = [0] * m
	    j = 0
	    
	    for i in range(1, m):
	        while j > 0 and P[i] != P[j]:
	            j = lps[j - 1]

	        if P[i] == P[j]:
	            j += 1
	            
	        lps[i] = j
	    return lps

	def solve(self, A):
		lps = self.calc_LPS_Array(A+'$'+A[::-1])
		return len(A) - lps[-1]
    
    
##FAstest
class Solution:
# @param A : string
# @return an integer
def solve(self, A):
    ch = 0
    i = 0
    j = len(A)-1
    while i<j:
        if A[i] == A[j]:
            i+=1
            j-=1
        else:
            if i==0:
                ch+=1
                j-=1
            else:
                ch+=i
                i =0
    return ch
##Shortest
class Solution:
    # @param A : string
    # @return an integer
    
    def solve(self, A):
        count =0
        for j in range(len(A),0,-1):
            s = A[0:j]
            if not s == s[::-1]:
                count+=1
            elif s == s[::-1]:
                break
        return count
    
    
            
