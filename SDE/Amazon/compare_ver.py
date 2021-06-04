class Solution:
 
    def compareVersion(self, A, B):
        ver1 = list(map(int, A.split(".")))
        ver2 = list(map(int, B.split(".")))
        if len(ver1)<len(ver2):
            ver1 += ([0] * (len(ver2) - len(ver1)))
        else:
            ver2 += ([0] * (len(ver1) - len(ver2)))
            
        for i in range(len(ver1)):
            if ver1[i] < ver2[i]:
                return -1
            if ver1[i] > ver2[i]:
                return 1
        return 0
