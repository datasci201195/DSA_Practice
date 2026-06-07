from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Linear Solution O(n)
        res = 0
        left, r = 0, len(heights) - 1

        while left < r:
            area = (r-left) * max(heights[left], heights[r])
            res = max(area,res)

            if heights[left] < heights[r]:
                left += 1
            else:
                r -= 1

        return res
                 