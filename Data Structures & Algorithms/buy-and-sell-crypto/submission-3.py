class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        left=0
        for right in range(1,len(prices)):
            if prices[left]>prices[right]:
                left=right
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                max_profit=max(max_profit,profit)
        return max_profit

            