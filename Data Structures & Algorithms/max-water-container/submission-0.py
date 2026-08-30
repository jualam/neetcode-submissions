class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                water=(min(heights[i],heights[j]))*(j-i)
                maxwater=max(maxwater,water)
        return maxwater