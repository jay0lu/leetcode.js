# https://leetcode.com/problems/longest-palindromic-substring/

def check_palindrome(str):
    if len(str) > 1:
        if str[0] == str[-1]:
            if len(str[1:-1]) > 0:
                check_palindrome(str[1:-1])
                return True
        else:
            return False
    else:
        return True


# class Solution(object):
#     def longestPalindrome(self, s):
#
#         # dynamic programming
#         if len(s) < 2:
#             return s
#         else:
#             slide_window = 1
#             i = 0
#             j = 0
#             while i+slide_window < len(s):
#                 j = i + slide_window
#                 for x in range (0,len(s)):
#                     # check_palindrome(s[i:j])
#                     pass

s = "abc"
print(check_palindrome(s))
