class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        low = 0
        high = len(height) - 1
        maxsquare = 0
        while high > low:
            h = height[low] if height[high] > height[low] else height[high]
            s = (high - low) * h
            if s > maxsquare:
                maxsquare = s
            if height[high] > height[low]:
                low += 1
            else:
                high -= 1

        return maxsquare
        
