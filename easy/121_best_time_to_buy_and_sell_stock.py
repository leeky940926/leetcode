from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = max_p = 0
        
        for i in range(1, len(prices)) :
            current_profit = prices[i] - prices[i-1]
            
            profit = max(current_profit, profit+current_profit)
            max_p = max(max_p, profit)
        
        return max_p