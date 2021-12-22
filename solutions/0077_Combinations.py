from utils import timer

class Solution:

    # Solution 1: Recursive
    # @timer
    # def combine(self, n, k):
    #     def combine_helper(start, answer_stack):
    #         if len(answer_stack) == k:
    #             answer.append(answer_stack)

    #         for i in range(start, n+1):
    #             combine_helper(i + 1, answer_stack + [i])

    #         return answer
        
    #     answer = []
    #     return combine_helper(1, [])
    
    # Solution 2: Backtracking
    @timer
    def combine(self, n, k):
        def combine_helper(start, answer_stack):
            if len(answer_stack) == k:
                answer.append(answer_stack[::])

            for i in range(start, n+1):
                answer_stack.append(i)
                combine_helper(i + 1, answer_stack)
                answer_stack.pop()

            return answer
        
        answer = []
        return combine_helper(1, [])


if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(n=4, k=2))
    print(sol.combine(n=1, k=1))