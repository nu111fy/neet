class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for n in nums:
            if n not in hash:
                hash[n] = 1
            else:
                return True
        return False
