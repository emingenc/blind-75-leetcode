from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = float('inf')
        max_profit = float('-inf')

        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)
        return max_profit


""" Here is the explanation for the code above:
1. We can have 2 variables: min_price and max_profit.
2. min_price is the minimum price we have seen so far, and max_profit is the maximum profit we can get.
3. We iterate through the prices and update min_price and max_profit accordingly.
4. We return max_profit.
 """
