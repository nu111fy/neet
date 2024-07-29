class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the variable to store the maximum area
        res = 0

        # Initialize two pointers, one at the start and one at the end of the array
        l, r = 0, len(height) - 1

        # Continue until the pointers meet
        while l < r:
            # Calculate the area between the current two lines
            # Area is width (r-l) times the height of the shorter line
            area = (r - l) * min(height[l], height[r])

            # Update the maximum area if the current area is larger
            res = max(res, area)

            # Move the pointer pointing to the shorter line
            # This is because moving the pointer of the taller line will never increase the area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        # Return the maximum area found
        return res
