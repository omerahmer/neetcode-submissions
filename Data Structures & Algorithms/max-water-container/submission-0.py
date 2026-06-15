class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            min_height = min(heights[left], heights[right])
            res = max(res, min_height * width)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
        return res