class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        C = sort(A)
        for i in range(len(A)):
            if(C[i]+1!=i+1):
                return C[i]+1
                
