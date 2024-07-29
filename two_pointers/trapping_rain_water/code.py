class Solution:
    def trap(self, height: List[int]) -> int:
        # Initialize two pointers, one at the start and one at the end of the array
        l, r = 0, len(height) - 1

        # Initialize variables to keep track of the maximum height seen from left and right
        leftMax, rightMax = height[l], height[r]

        # Initialize the result variable to store the total trapped water
        res = 0

        # Continue until the pointers meet
        while l < r:
            # If the left max is smaller, we process the left side
            if leftMax < rightMax:
                # Move the left pointer inward
                l += 1
                # Update the left max height if we find a taller bar
                leftMax = max(leftMax, height[l])
                # Add the trapped water above the current bar
                # This is the difference between the leftMax and the current height
                res += leftMax - height[l]
            # If the right max is smaller (or equal), we process the right side
            else:
                # Move the right pointer inward
                r -= 1
                # Update the right max height if we find a taller bar
                rightMax = max(rightMax, height[r])
                # Add the trapped water above the current bar
                # This is the difference between the rightMax and the current height
                res += rightMax - height[r]

        # Return the total amount of trapped water
        return res
