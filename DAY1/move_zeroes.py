class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        j=len(nums)
        for i in range(j):
            if nums[i]!=0:
                nums[i],nums[s]=nums[s],nums[i]
                s+=1
        
