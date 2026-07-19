class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = deque()

        for c in s:
            if c in pairs: # we got a closer
                if not stack:
                    return False
                popped = stack.pop()
                if popped != pairs[c]:
                    return False
            else:
                stack.append(c)
        return not stack