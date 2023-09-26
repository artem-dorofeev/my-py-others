class Solution(object):
    def isSubsequence(self, s, t):
        result = ''
        # for i in s:
        #     if i not in t:
        #         return False
        #     print(result, s, t)
        #     result += i
        # # return True if result == s else False
        # print(f"result - {result}")
        # print(F"s - {s}")

        result = ''
        for a in t:
            if a in s:
                result += a
            # print(result)
        if result == s:
            return True

        return False
        # if result != s:
        #     return True
        # return False
  

if __name__ == "__main__":
    s = "acb" 
    t = "ahbgdc"
    # test_str = 'cbacdcbc'
    test = Solution()
    print(test.isSubsequence(s, t))
    # s.romanToInt(test_str)

"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

 
Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

 
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?
"""