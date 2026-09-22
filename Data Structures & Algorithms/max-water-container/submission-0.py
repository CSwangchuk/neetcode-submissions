class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p_1 = 0
        p_2 = len(heights)-1
        highest = 0
        while p_1<p_2:
            width = p_2-p_1
            height = min(heights[p_1],heights[p_2])
            area = width*height
            highest = max(highest,area)

            if heights[p_1]<heights[p_2]:
                p_1+=1
            else:
                p_2-=1
        
        return highest
        