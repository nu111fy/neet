class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in hash:
                hash[key] = [s]
            else:
                hash[key].append(s)
        return hash.values()
