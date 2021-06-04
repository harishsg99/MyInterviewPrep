class Solution:

    def restoreIpAddresses(self, A):
        K = 3
        c = []
        res = [int(A[idx : idx + K]) for idx in range(0, len(A), K)]
        for i in range(len(res)):
            if(0<=res[i]<=255):
                
                b = ".".join(res[i])
                c.append(b)
        return c
                
            
