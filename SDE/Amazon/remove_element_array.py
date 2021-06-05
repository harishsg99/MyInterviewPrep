class Solution:
    def removeElement(self, A, B):
        c = []
        for i in range(len(A)):
            if(A[i]!==B):
                c.append(A[i])
        return len(c)
                
