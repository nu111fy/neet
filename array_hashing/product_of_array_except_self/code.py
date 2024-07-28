class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with 1s, same length as nums
        res = [1] * (len(nums))

        # Calculate prefix products
        # Each element in res will be the product of all numbers to its left
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        # Initialize postfix product as 1
        postfix = 1

        # Calculate postfix products and combine with prefix products
        # Iterate through the array from right to left
        for i in range(len(nums) - 1, -1, -1):
            # Multiply current result by postfix product
            res[i] *= postfix
            # Update postfix product for next iteration
            postfix *= nums[i]

        # Return the final result array
        return res
