class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Initialize a dictionary to store the frequency of each character in s1
        s1_hash = {}
        for letter in s1:
            # Increment the count of the character in the dictionary
            s1_hash[letter] = 1 + s1_hash.get(letter, 0)

        # Initialize the left pointer of the sliding window to 0
        l = 0
        # Iterate over each character in s2 with the right pointer
        for r in range(len(s2)):
            # Decrement the count of the current character in the dictionary
            s1_hash[s2[r]] = s1_hash.get(s2[r], 0) - 1
            # If the count of the current character is less than 0, adjust the window
            while s1_hash[s2[r]] < 0:
                # Increment the count of the character at the left pointer
                s1_hash[s2[l]] += 1
                # Move the left pointer to the right, shrinking the window
                l += 1
            # Check if the current window size matches the length of s1
            if (r - l + 1 == len(s1)):
                # If it does, return True indicating a permutation of s1 is found in s2
                return True
        # If no permutation is found, return False
        return False
