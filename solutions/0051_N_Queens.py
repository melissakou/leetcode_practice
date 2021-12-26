from utils import timer

class Solution:

    # Solution 1: Backtracking (use the diagonal index)
    @timer
    def solveNQueens(self, n):
        answer, has_queen_col, left_diagonal, right_diagonal = [], [], set(), set()
		
        def place_queen(row):
            if row == n:
                answer.append(['.'*c + 'Q' + '.'*(n-c-1) for c in has_queen_col])

            for c in range(n):
                if not c in has_queen_col and not row + c in left_diagonal and not row - c in right_diagonal:
                    has_queen_col.append(c)
                    left_diagonal.add(row + c)
                    right_diagonal.add(row - c)
                    place_queen(row + 1)
                    has_queen_col.pop()
                    left_diagonal.remove(row + c)
                    right_diagonal.remove(row - c)
            
        place_queen(0)
        return answer



if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))
    print(sol.solveNQueens(1))