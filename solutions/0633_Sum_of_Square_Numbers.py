from utils import timer

class Solution:

    # Solution 1: Two Pointer
    # @timer
    # def judgeSquareSum(self, c):
    #     a, b = 0, int(c**0.5)+1
    #     while a <= b:
    #         curr_square_sum = a ** 2 + b ** 2
    #         if curr_square_sum == c: return True
    #         elif curr_square_sum < c: a += 1
    #         elif curr_square_sum > c: b -= 1
        
    #     return False

    # Solution 2: Store seen
    # @timer
    # def judgeSquareSum(self, c):
    #     serach = list(range(int(c ** 0.5) + 1))
    #     seen_square = set()
    #     for s in serach:
    #         remain = c - s ** 2
    #         seen_square.add(s ** 2)
    #         if remain in seen_square: return True
        
    #     return False

    # Solution 3: Sum of Two Squares Theorem
    @timer
    def judgeSquareSum(self, c):
        prime = 2
        while prime * prime <= c:
            k = 0
            while c % prime == 0:
                k += 1
                c = c // prime
            if k != 0 and prime % 4 == 3 and k % 2 == 1:
                return False
            prime += 1
        
        return c % 4 != 3

if __name__ == "__main__":
    sol = Solution()
    print(sol.judgeSquareSum(5))
    print(sol.judgeSquareSum(3))
    print(sol.judgeSquareSum(4))
    print(sol.judgeSquareSum(2))
    print(sol.judgeSquareSum(1))