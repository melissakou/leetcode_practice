from utils import timer

class Solution:

    # Solution 1: Greedy + Two Pointer
    @timer
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        num_content, g_pointer, s_pointer = 0, 0, 0
        while g_pointer < len(g) and s_pointer < len(s):
            if g[g_pointer] <= s[s_pointer]:
                num_content += 1 ; g_pointer += 1 ; s_pointer += 1
            else:
                s_pointer += 1
        
        return num_content


if __name__ == "__main__":
    sol = Solution()
    print(sol.findContentChildren(g=[1, 2, 3], s=[1, 1]))
    print(sol.findContentChildren(g=[1, 2], s=[1, 2, 3]))