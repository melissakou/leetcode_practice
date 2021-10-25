from utils import timer

class Solution:

    # Solution 1: Two Pointer
    # @timer
    # def validPalindrome(self, s):
    #     left, right = 0, len(s)-1
    #     while left <= right:
    #         if s[left] != s[right]:
    #             del_left = s[:left] + s[left+1:]
    #             del_right = s[:right] + s[right+1:]
    #             return del_left == del_left[::-1] or del_right == del_right[::-1]
    #         left += 1 ; right -= 1
        
    #     return True

    # Solurion 2: Two Pointers + Recursive
    @timer
    def validPalindrome(self, s):
        def check_palindrome(left, right, delete):
            while left <= right:
                if s[left] != s[right]:
                    if delete: return False
                    else:
                        return check_palindrome(left+1, right, True) or check_palindrome(left, right-1, True)
                left += 1 ; right -= 1
            
            return True

        return check_palindrome(0, len(s)-1, False)


if __name__ == "__main__":
    sol = Solution()
    print(sol.validPalindrome("aba"))
    print(sol.validPalindrome("abca"))
    print(sol.validPalindrome("abc"))