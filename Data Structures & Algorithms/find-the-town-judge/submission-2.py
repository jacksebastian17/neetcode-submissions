class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        scores = [0] * (n + 1)
        for a, b in trust:
            scores[a] -= 1
            scores[b] += 1
        for i in range(len(scores)):
            if scores[i] == n-1:
                return i
        return -1