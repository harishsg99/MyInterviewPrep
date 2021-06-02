class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        b = []
        for i in range(len(A)):
            for j in range(len(A)):
                if(A[i] <= A[j]):
                    c = j-i
                    b.append(c)
        return max(b)
