# 1.naive solution – double nested loop

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#
#         maxProf = 0
#         n = len(prices)
#         for i in range(n - 1):
#             for j in range(i+1, n):
#                 if prices[j] - prices[i] > maxProf:
#                     maxProf  = prices[j] - prices[i]
#         return maxProf

# 2. O(n) and O(1) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        min_price = prices[0]

        for price in prices[1:]:
            maxProf = max(maxProf, price - min_price)
            min_price = min(min_price, price)

        return maxProf
