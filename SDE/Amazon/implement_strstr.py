class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if(len(A)!=0 and len(B)!=0):
            try:
                c = A.index(B)
                return c
            except ValueError as ve:
                return -1
        else:
            return -1
