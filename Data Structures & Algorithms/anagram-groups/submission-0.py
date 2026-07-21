class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs: # s: act
            count = [0] * 26
            for c in s: # a
                index = ord(c) - ord("a")
                count[index] += 1
            # [1, 0, 1, ..., 1, ..., 0]
            #  a     c       t
            key = tuple(count) # (1, 0, 1, ..., 1, ..., 0)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)
        
        return list(groups.values())