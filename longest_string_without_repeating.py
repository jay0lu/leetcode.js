# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """

        longest_len = 0
        for a in range(0,len(s)):
            list = []
            list.append(s[a])

            for b in range(a+1,len(s)):
                if not s[b] in list:
                    list.append(s[b])
                    print(list)
                else: break

            if len(list) > longest_len:
                longest_len = len(list)

        return longest_len


str = "abcabcbb"
str2 = "aaaaaaa"
str3 = "pwwkew"
str4 = "abdddce"
str5 = "addccccddddddd"
solution = Solution()
length = solution.lengthOfLongestSubstring(str5)
print("longest length is %s" % length)
