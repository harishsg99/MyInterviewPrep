import math
class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        if (int(A) == 0):
            return 0
        while (int(A) != 1):
            if (int(A) % 2 != 0):
                return False
                A=int(A// 2)
             
        return 1
                
