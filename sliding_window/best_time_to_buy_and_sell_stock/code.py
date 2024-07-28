class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, minS = -float('inf'), prices[0]
        for p in prices:
            maxP = max(maxP, p-minS)
            minS = min(p, minS)
        return maxP
