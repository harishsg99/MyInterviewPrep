class Solution:
# @param A : list of integers
# @param B : integer
# @return an integer
def solve(self, A, B):
    ans = 0
    zeros = []
    zn = 0
    n = len(A)
    for i in range(n):
        if A[i]==0:
            zeros.append(i)
            zn += 1
        if zn<=B:
            ans = max(ans,i+1)
        else:
            ans = max(ans,i-zeros[zn-1-B])
    return ans
