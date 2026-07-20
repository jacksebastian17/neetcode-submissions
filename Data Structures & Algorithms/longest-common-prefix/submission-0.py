class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        shortest_length = min(len(s) for s in strs)
        while i < shortest_length: # while 0 < 3
            c = strs[0][i]
            for s in strs: # bat, bag
                if s[i] != c: # bat[0] = b != b, return,,,, bag[0] = b != b return
                    return prefix
            prefix += c
            i += 1
        return prefix

