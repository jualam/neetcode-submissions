class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_num=prices[0]
        for num in prices:
            min_num=min(min_num,num)
            max_profit=max(max_profit, num-min_num)
        return max_profit
