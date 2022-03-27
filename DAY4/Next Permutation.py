class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos1 = -1
        for i in range(n - 2, -1, -1): 
            if nums[i] < nums[i + 1]:
                pos1 = i
                break
        if pos1 >= 0:
            for i in range(n - 1, pos1, -1):  
                if nums[pos1] < nums[i]:
                    nums[pos1], nums[i] = nums[i], nums[pos1]
                    break
        i, j = pos1 + 1, n - 1
        while i < j:  
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
		
