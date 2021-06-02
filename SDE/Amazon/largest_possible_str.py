from itertools import permutations
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        lst = []
        for i in permutations(A, len(A)):
            # provides all permutations of the list values,
            # store them in list to find max
            lst.append("".join(map(str,i)))
        return str(max(lst))
