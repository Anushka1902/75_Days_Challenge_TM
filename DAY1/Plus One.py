class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in range(len(digits)):
            s+=str(digits[i])   
        s=int(s)
        ans=s+1
        ans=str(ans)
        nums=[]
        for i in ans:
            nums.append(i)
        return nums
