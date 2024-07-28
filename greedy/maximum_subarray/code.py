class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float("-inf")
        max_till_here = 0
        for i in range(len(nums)):
            max_till_here += nums[i]
            if max_so_far < max_till_here:
                max_so_far = max_till_here
            if max_till_here < 0:
                max_till_here = 0
        return max_so_far
