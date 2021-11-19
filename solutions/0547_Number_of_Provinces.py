from utils import timer
from my_algorithms.union_find import UnionFind

class Solution:

    # Solution 1: DFS
    # @timer
    # def findCircleNum(self, isConnected):
    #     n = len(isConnected)
    #     visited = []

    #     def traverse(i):
    #         visited.append(i)
    #         for j in range(n):
    #             if isConnected[i][j] and j not in visited: traverse(j)

    #     result = 0
    #     for i in range(n):
    #         if i not in visited:
    #             result += 1
    #             traverse(i)
    #     return result

    # Solution 2: Union-Find
    @timer
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] and uf.find(i) != uf.find(j):
                    uf.union(i, j)

        return len(set([uf.find(i) for i in range(n)]))
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print(sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))