from utils import timer

class Solution:

    # Solution 1: Greedy: find peak & valley
    @timer
    def maxProfit(self, prices):
        profit, buy = 0, None

        for i in range(len(prices)):
            if i == len(prices) - 1:
                if buy is not None: profit += (prices[i] - buy)
            elif prices[i] > prices[i+1] and buy is not None:
                profit += (prices[i] - buy) ; buy = None
            elif prices[i] < prices[i+1] and buy is None:
                buy = prices[i]

        return profit

    # Solution 2: Greedy: every greedy
    # @timer
    # def maxProfit(self, prices):
    #     profit = 0
    #     for i in range(len(prices)-1):
    #         slope = prices[i+1] - prices[i]
    #         if slope > 0: profit += slope
        
    #     return profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([1,2,3,4,5]))
    print(sol.maxProfit([7,6,4,3,1]))