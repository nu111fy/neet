class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for n in nums:
            if n not in hash:
                hash[n] = 1
            else:
                hash[n] += 1

        print(hash)
        temp = sorted(hash.items(), key=lambda x: -x[1])
        res = []
        for i in range(k):
            res.append(temp[i][0])
        return res
