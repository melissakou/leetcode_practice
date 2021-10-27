from utils import timer

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    @timer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0: return 0
        left, distinct, max_len, stat = 0, 0, 0, {}
        for right in range(len(s)):
            stat[s[right]] = stat.get(s[right], 0) + 1
            if stat[s[right]] == 1: distinct += 1
            while distinct > k and left < right:
                stat[s[left]] = stat[s[left]] - 1
                if stat[s[left]] == 0:
                    distinct -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len



if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct(s="eceba", k=3))
    print(sol.lengthOfLongestSubstringKDistinct(s="WORLD", k=4))