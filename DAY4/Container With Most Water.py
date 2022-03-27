class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,ans = 0,len(height)-1,0
        while l<r:
            a=min(height[l],height[r])
            b=r-l
            ans=max(ans,a*b)
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return ans
