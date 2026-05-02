class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i+1
        res = 0
        while i<=j and j<len(prices):
            profit =  prices[j] - prices[i]
            if profit >= 0:
                j+=1
            else:
                i+=1
            res = max(profit,res)
        if res<0:
            return 0
        else:
            return res