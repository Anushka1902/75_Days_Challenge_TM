class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numsLen = len(nums)
        ht = {}
        runningSum = 0
        subarrays = 0
        for i in range(numsLen):
            runningSum += nums[i]
            if runningSum == k:
                subarrays += 1
            if runningSum - k in ht:
                subarrays += ht[runningSum - k]
            if runningSum not in ht:
                ht[runningSum] = 0
            ht[runningSum] += 1
        return subarrays
