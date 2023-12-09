class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        current_profit =0
        for i in range(1,len(prices)):
             current_profit = max(0, current_profit + prices[i] - prices[i-1])
             max_profit =max(max_profit,current_profit)
        return max_profit
        

       