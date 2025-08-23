'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
'''

##  SLIDING WINDOW

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):    
            left_min = min(left_min, prices[i-1])
            max_profit = max(max_profit, prices[i] - left_min)
        return max_profit