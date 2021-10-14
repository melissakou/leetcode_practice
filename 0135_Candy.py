from utils import timer

class Solution:

    # Solution 1: Greedy
    @timer
    def candy(self, ratings):
        if len(ratings) == 1:
            return 1
        candy = [1] * len(ratings)
        for i in range(0, len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                candy[i+1] = candy[i] + 1
        for i in range(1, len(ratings))[::-1]:
            if ratings[i-1] > ratings[i] and candy[i-1] <= candy[i]:
                candy[i-1] = candy[i] + 1
        
        return sum(candy)

    # Solurion 2
    # @timer
    # def candy(self, ratings):
    #     pass




if __name__ == "__main__":
    sol = Solution()
    print(sol.candy([1,0,2]))
    print(sol.candy([1,2,2]))