class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0] # 10
        profit = 0
        for p in prices:
            if p < buy:
                buy = p
            total = p - buy
            if total > profit:
                profit = total
        return profit
