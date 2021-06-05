class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
            A.sort()
            c = len(A)
            for i  in range(len(A)):
                if(A[i]+B==A[i+1]):
                    return 1
                else:
                    return 0
