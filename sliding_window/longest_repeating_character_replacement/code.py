class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize a dictionary to count the frequency of characters in the current window
        count = {}

        # Initialize the variable to store the length of the longest valid window
        res = 0

        # Initialize the left pointer of the window
        l = 0

        # Iterate over each character in the string using the right pointer r
        for r in range(len(s)):
            # Increment the frequency of the current character s[r] in the count dictionary
            count[s[r]] = 1 + count.get(s[r], 0)

            # Check if the current window size minus the max frequency character count exceeds k
            if (r - l + 1) - max(count.values()) > k:
                # If it does, decrement the count of the character at the left pointer
                count[s[l]] -= 1

                # Move the left pointer to the right to shrink the window
                l += 1

            # Update the result with the maximum length of the valid window
            res = max(res, r - l + 1)

        # Return the length of the longest valid window found
        return res
