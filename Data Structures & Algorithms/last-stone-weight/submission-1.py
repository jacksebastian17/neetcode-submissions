class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            stone1, stone2 = stones[0], stones[1]
            smashed = abs(stone1 - stone2)
            if smashed == 0:
                stones = stones[2:]
                continue
            stones = stones[2:]
            stones.append(smashed)
        if len(stones) == 0:
            return 0
        return stones[0]
            