class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a set to keep track of characters in the current window
        charSet = set()

        # Initialize the left pointer of the sliding window
        l = 0

        # Initialize the variable to store the length of the longest substring
        res = 0

        # Iterate through the string with the right pointer
        for r in range(len(s)):
            # If the current character is already in the set,
            # remove characters from the left until we remove the duplicate
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # Add the current character to the set
            charSet.add(s[r])

            # Update the length of the longest substring if necessary
            # Current substring length is (r - l + 1)
            res = max(res, r - l + 1)

        # Return the length of the longest substring without repeating characters
        return res
