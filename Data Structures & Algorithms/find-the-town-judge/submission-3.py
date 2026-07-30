class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        scores = [0] * (n + 1)
        for a, b in trust:
            scores[a] -= 1 # deduct 1 for person ai since theyre trusting someone
            scores[b] += 1 # add 1 for person bi since theyre being trusted by someone
        print(scores)
        # town judge will be the one where their score is equal to n - 1
        for i in range(len(scores)):
            if scores[i] == n - 1:
                return i
        return -1