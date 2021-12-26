import collections
from functools import reduce
from itertools import product
from utils import timer

def add(a,b):
    return a + b

def my_or(a,b):
    return a or b

class Solution:

    # Solution 1: DFS - Backtracking
    @timer
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        if m == 1 and n == 1 and board[0][0] == word:
            return True

        board_stat = collections.Counter(reduce(add, board))
        word_stat = collections.Counter(word)
        for c in word_stat.keys():
            if word_stat[c] > board_stat.get(c, 0):
                return False        

        def traverse(i, j, target):
            if len(target) == 0:
                return True
            if i < 0 or j < 0 or i >= m or j >= n or (i,j) in visited:
                return False
            
            if board[i][j] == target[0]:
                walk = []
                for step in [(-1,0), (1,0), (0,-1), (0,1)]:
                    visited.add((i,j))
                    walk.append(traverse(i+step[0], j+step[1], target[1:]))
                    visited.remove((i,j))

                return reduce(my_or, walk)

            return False

        for i,j in product(range(m), range(n)):
            visited = set()
            if traverse(i, j, word):
                return True

        return False

    

if __name__ == "__main__":
    sol = Solution()
    print(sol.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED"))
    print(sol.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="SEE"))
    print(sol.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCB"))