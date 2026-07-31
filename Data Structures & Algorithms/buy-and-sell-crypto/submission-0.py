class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # naive solution – double nested loop
        maxProf = 0
        n = len(prices)
        for i in range(n - 1):
            for j in range(i+1, n):
                if prices[j] - prices[i] > maxProf:
                    maxProf  = prices[j] - prices[i]

        return maxProf



sol = Solution()
print(sol.maxProfit([10,8,7,5,2]))
