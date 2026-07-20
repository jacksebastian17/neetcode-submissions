class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest_length = min(len(s) for s in strs)
        for i in range(shortest_length):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return prefix
            prefix += c
        return prefix

