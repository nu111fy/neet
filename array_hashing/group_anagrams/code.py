class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize an empty dictionary to store anagram groups
        hash = {}

        # Iterate through each string in the input list
        for s in strs:
            # Sort the characters of the string and join them to create a key
            key = "".join(sorted(s))

            # If the key doesn't exist in the dictionary
            if key not in hash:
                # Create a new list with the current string as its only element
                hash[key] = [s]
            # If the key already exists in the dictionary
            else:
                # Append the current string to the existing list
                hash[key].append(s)

        # Return all the values (lists of anagrams) from the dictionary
        return hash.values()
