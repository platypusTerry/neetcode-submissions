class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            if heights[left] < heights[right]:
                area = max(area, (right-left) * heights[left])
                left += 1

            elif heights[left] > heights[right]:
                area = max(area, (right-left) * heights[right])
                right -= 1

            else: #heights[left] == height[right]
                area = max(area, (right-left) * heights[right])
                right -= 1
        return area