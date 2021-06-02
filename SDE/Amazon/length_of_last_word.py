class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        return len(A.strip().split(' ')[-1])
      
