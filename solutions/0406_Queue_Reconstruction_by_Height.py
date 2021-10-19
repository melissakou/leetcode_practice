from utils import timer

class Solution:

    # Solution 1: Greedy
    @timer
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
    print(sol.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))