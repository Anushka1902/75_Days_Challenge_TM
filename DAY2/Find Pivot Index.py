class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        for i in range(len(nums)):
            if (sum(nums[:i]) == sum(nums[i+1:])):
                return i
        return -1
        '''
        l=0
        rs=sum(nums)
        for i in range(len(nums)):
            l+=nums[i]
            rs-=nums[i]
            if l-nums[i]==rs:
                return i
        return -1
