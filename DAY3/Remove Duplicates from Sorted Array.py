class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        l = list(set(nums))
        l.sort()
        for i in range(len(l)):
            nums[i] = l[i]
        return len(l)
        '''
        i = 0
        for j in range(len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
