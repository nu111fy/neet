class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = s.lower()
        left = 0
        right = len(palin)-1
        while left < right:
            while left < right and not palin[left].isalnum():
                left += 1
            while left < right and not palin[right].isalnum():
                right -= 1
            if palin[left] != palin[right]:
                return False
            left += 1
            right -= 1
        return True
