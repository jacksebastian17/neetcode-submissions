class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(','{','[']
        close = [')','}',']']
        pairs = {')': '(', '}': '{', ']': '['}

        stack = deque()
        for c in s:
            if c in open:
                stack.append(c)
            elif c in close:
                if (len(stack) == 0):
                    return False
                popped = stack.pop() # popped = {, c = }
                if pairs[c] != popped:
                    return False
        if len(stack) == 0:
            return True
        return False