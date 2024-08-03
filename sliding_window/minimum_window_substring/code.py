class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is an empty string, return an empty string as there's nothing to find
        if t == "":
            return ""

        # Dictionaries to store the frequency of characters in t and the current window in s
        countT, window = {}, {}

        # Populate countT with the frequency of each character in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Initialize variables to keep track of how many characters have been matched
        have, need = 0, len(countT)
        # Result variables to store the start and end indices of the minimum window and its length
        res, resLen = [-1, -1], float("inf")
        # Left pointer of the window
        l = 0

        # Iterate over the string s with the right pointer
        for r in range(len(s)):
            c = s[r]
            # Increment the count of the current character in the window
            window[c] = 1 + window.get(c, 0)

            # If the current character is in t and its count in the window matches its count in t
            if c in countT and window[c] == countT[c]:
                have += 1

            # If all characters in t are matched in the current window
            while have == need:
                # Update the result if the current window is smaller than the previously found window
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # Decrement the count of the character at the left pointer in the window
                window[s[l]] -= 1
                # If the character at the left pointer is in t and its count in the window is less than its count in t
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # Move the left pointer to the right, shrinking the window
                l += 1

        # Extract the start and end indices of the minimum window
        l, r = res
        # Return the minimum window substring if a valid window was found, otherwise return an empty string
        return s[l: r + 1] if resLen != float("inf") else ""
