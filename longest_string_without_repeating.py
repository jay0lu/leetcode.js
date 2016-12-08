# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """

        longest_len = 1
        for a in range(0,len(s)):
            list = []
            list.append(s[a])

            for b in range(a+1,len(s)):
                if not s[b] in list:
                    list.append(s[b])
                    print(list)

            if len(list) > longest_len:
                longest_len = len(list)

        print("longest length is %s" % longest_len)


str = "abcabcbb"
str2 = "aaaaaaa"
Solution.lengthOfLongestSubstring(str)
