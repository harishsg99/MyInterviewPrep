class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedArray=sorted(nums) 
        if nums==sortedArray:
            return 0
        i,c=0,0
        while nums[i]==sortedArray[i] and i<len(nums):
            i+=1
            c+=1
        j=len(nums)-1
        while nums[j]==sortedArray[j] and j>-1:
            j-=1
            c+=1
        return len(nums)-c
