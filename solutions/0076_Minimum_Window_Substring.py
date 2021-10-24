from utils import timer

class Solution:

    # Solution 1: Two Pointers, Sliding Window
    @timer
    def minWindow(self, s, t):
        if len(t) > len(s): return ""
        t_stat, curr_stat = {}, {}
        for x in t: t_stat[x] = t_stat.get(x, 0) + 1
        num_match, result, min_len, l = 0, [-1, -1], float("infinity"), 0
        for r, c in enumerate(s):
            if c in t_stat.keys():
                curr_stat[c] = curr_stat.get(c, 0) + 1
                if curr_stat[c] == t_stat[c]: num_match += 1
                while num_match == len(t_stat):
                    if r-l+1 < min_len: result, min_len = [l, r], r-l+1
                    pop_c = s[l]
                    if pop_c in t_stat.keys():
                        curr_stat[pop_c] = curr_stat[pop_c] - 1
                        if curr_stat[pop_c] < t_stat[pop_c]: num_match -= 1
                    l += 1

        return s[result[0]:result[1]+1]



if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(sol.minWindow(s="a", t="a"))
    print(sol.minWindow(s="a", t="aa"))