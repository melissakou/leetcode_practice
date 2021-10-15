from utils import timer

class Solution:

    # Solution 1: Greedy, Check every position
    # @timer
    # def canPlaceFlowers(self, flowerbed, n):
    #     flowerbed = [0] + flowerbed + [0]
        
    #     i = 1
    #     while i < len(flowerbed)-1 and n > 0:
    #         if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
    #             flowerbed[i] = 1 ; n -= 1
    #         i += 1

    #     return n == 0

    # Solution 2: Greedy, Jump position.
    @timer
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = flowerbed + [0]
        i = 1
        while i < len(flowerbed)-1 and n > 0:
            if flowerbed[i] == 1:
                i += 2 ; continue
            if flowerbed[i+1] == 0:
                n -= 1 ; i += 2
            else: i += 1

        return n == 0



if __name__ == "__main__":
    sol = Solution()
    print(sol.canPlaceFlowers(flowerbed=[1,0,0,0,1], n=1))
    print(sol.canPlaceFlowers(flowerbed=[1,0,0,0,1], n=2))