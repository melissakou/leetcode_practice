import re
from utils import timer

class Solution:

    # Solution 1: Two Pointers
    # @timer
    # def findLongestWord(self, s, dictionary):
    #     dictionary = sorted(dictionary, key=lambda x: (-len(x), x))
    #     for target in dictionary:
    #         s_pointer, target_pointer = 0, 0
    #         while s_pointer < len(s) and target_pointer < len(target):
    #             if s[s_pointer] == target[target_pointer]: target_pointer += 1
    #             s_pointer += 1
    #         if target_pointer >= len(target): return target
    #     return ""

    # Solution 2: Two Pointers, using string.find()
    @timer
    def findLongestWord(self, s, dictionary):
        dictionary = sorted(dictionary, key=lambda x: (-len(x), x))
        for target in dictionary:
            s_pointer, target_pointer = 0, 0
            while s_pointer < len(s) and target_pointer < len(target):
                if s[s_pointer] == target[target_pointer]:
                    s_pointer += 1 ; target_pointer += 1
                else:
                    next_pointer = s.find(target[target_pointer], s_pointer+1)
                    if next_pointer == -1: break
                    else: s_pointer = next_pointer+1 ; target_pointer += 1
            if target_pointer >= len(target): return target
        return ""




if __name__ == "__main__":
    sol = Solution()
    print(sol.findLongestWord("abpcplea",["ale","apple","monkey","plea", "abpcplaaa","abpcllllll","abccclllpppeeaaaa"]))
    print(sol.findLongestWord(s="abpcplea", dictionary=["a", "b", "c"]))