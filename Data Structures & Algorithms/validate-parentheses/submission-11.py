class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []

        for c in s:
            if c in pairs: # we got a closing bracket
                if not stack or stack.pop() != pairs.get(c):
                    return False
            else:
                stack.append(c)
        return not stack