class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            curr_profit = i - min_price
            if curr_profit > max_profit:
                max_profit = curr_profit
            if min_price > i:
                min_price = i
        return max_profit
        #Version 2
        # buy, sell = 0, 1
        # max_profit = 0
        # while sell < len(prices):
        #     if prices[buy] < prices[sell]:
        #         profit = prices[sell] - prices[buy]
        #         max_profit = max(max_profit, profit)
        #     else:
        #         buy = sell
        #     sell += 1
        # return max_profit            

                
   
   
   












