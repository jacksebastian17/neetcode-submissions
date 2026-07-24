class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            smashed = stone1 - stone2
            if smashed == 0:
                continue
            heapq.heappush(heap, smashed)
        if len(heap) == 0:
            return 0
        return abs(heapq.heappop(heap))
