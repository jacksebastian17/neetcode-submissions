class Solution:
    def reorganizeString(self, s: str) -> str:
        # s = "aaabbc"
        counts = Counter(s)
        # counts = {'a': 3, 'b': 2, 'c': 1}
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""
        heap = [(-c, ch) for ch, c in counts.items()]
        heapq.heapify(heap)
        # heap = [(-3,'a'), (-2,'b'), (-1,'c')]
        # ab
        # heap = [(-2,'a'), (-1,'b'), (-1,'c')]
        # abab
        # heap = [(-1,'a'), (-1,'c')]
        # ababac
        result = []
        while len(heap) >= 2:
            c1, ch1 = heapq.heappop(heap)
            c2, ch2 = heapq.heappop(heap)
            result.append(ch1); result.append(ch2)
            if c1 + 1 < 0: heapq.heappush(heap, (c1 + 1, ch1))
            if c2 + 1 < 0: heapq.heappush(heap, (c2 + 1, ch2))
        if heap:
            result.append(heap[0][1])
        return "".join(result)