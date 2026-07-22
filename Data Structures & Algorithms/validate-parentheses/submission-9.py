class Solution:
    def isValid(self, s: str) -> bool:
        parenPairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for c in s:
            if c in parenPairs: # we got a closing bracket
                # stack = [ '[' ]
                if not stack:
                    return False
                popped = stack.pop() # [
                if parenPairs.get(c) != popped:
                    return False
            else:
                stack.append(c)
        return not stack