class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize the output list to store the maximums of each window
        output = []
        # Initialize a deque to store indices of elements in the current window
        q = collections.deque()
        # Initialize the left (l) and right (r) pointers of the sliding window
        l = r = 0

        # Iterate over the array with the right pointer
        while r < len(nums):
            # Remove elements from the deque if they are smaller than the current element
            # since they will not be the maximum in this window or any future window
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # Append the current element index to the deque
            q.append(r)

            # Remove the leftmost element from the deque if it's out of the window bounds
            if l > q[0]:
                q.popleft()

            # When the window size reaches k, record the maximum element (front of the deque)
            if (r + 1) >= k:
                # The front of the deque is the index of the maximum element in the current window
                output.append(nums[q[0]])
                # Move the left pointer to the right to shrink the window from the left
                l += 1

            # Move the right pointer to the right to expand the window
            r += 1

        # Return the list of maximums for each sliding window
        return output
