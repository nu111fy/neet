class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the input list to a set for O(1) lookup time
        numSet = set(nums)

        # Initialize the variable to store the length of the longest sequence
        longest = 0

        # Iterate through each number in the set
        for n in numSet:
            # Check if it's the start of a sequence
            # If n-1 is not in the set, n is the start of a sequence
            if (n - 1) not in numSet:
                # Initialize the length of the current sequence
                length = 1

                # Keep incrementing length while the next consecutive number exists
                while (n + length) in numSet:
                    length += 1

                # Update the longest sequence found so far
                longest = max(length, longest)

        # Return the length of the longest consecutive sequence
        return longest
