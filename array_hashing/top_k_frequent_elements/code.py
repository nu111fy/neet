class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize a dictionary to store the count of each number
        count = {}

        # Create a list of empty lists. The index represents the frequency,
        # and the list at that index will store numbers with that frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each number in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Populate the freq list: for each number and its count,
        # append the number to the list at the index of its count
        for n, c in count.items():
            freq[c].append(n)

        # Initialize the result list
        res = []

        # Iterate through freq list from right to left (highest frequency to lowest)
        for i in range(len(freq) - 1, 0, -1):
            # For each frequency, add all numbers with that frequency to the result
            for n in freq[i]:
                res.append(n)
                # If we've found k numbers, return the result
                if len(res) == k:
                    return res
