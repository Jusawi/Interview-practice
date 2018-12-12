class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_area, area = 0,0
        while(l<r):
            diff = r - l
            area = (diff * min(height[l], height[r]))
            if (height[l]< height[r] ):
                temp = height[l]
                while(height[l]<=temp):
                    l+=1
            else:
                temp = height[r]
                while(height[r]<=temp and l<r):
                    r-=1
            if (area> max_area):
                max_area = area
        return max_area
