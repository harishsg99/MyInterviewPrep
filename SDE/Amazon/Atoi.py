class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        for i in range(len(A)):
            if (A[i].isnumeric()==True):
                c = str(A[i]).strip()
                return c
