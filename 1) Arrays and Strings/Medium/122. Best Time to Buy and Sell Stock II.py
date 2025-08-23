'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

class Solution(object):
    def maxProfit(self, prices):
        i = 0       # main pointer
        n = 1       # second pointer
        length = len(prices)
        tot_profit = 0
        while n < length:
            if prices[n] > prices[n-1]:
                while n+1 < length and prices[n+1] > prices[n]:
                    n+=1
                tot_profit += prices[n] - prices[i]
            i = n 
            n += 1
        return tot_profit