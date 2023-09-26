class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = ''
        tempt_str = s[1::]
        for i in s:
            if i not in tempt_str:
                result += i
            tempt_str = tempt_str[1::]
        return result
        
        """result = ''
        test_str = s[1::]
        n = 0
        while n < len(s):
            if s[n] not in test_str:
                result += s[n]
            test_str = test_str[1::]
            n += 1
        return result"""

if __name__ == "__main__":
    test_str = 'cbacdcbc'
    s = Solution()
    print(s.removeDuplicateLetters(test_str))
    # s.romanToInt(test_str)

"""
316. Remove Duplicate Letters


Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order
among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

 

Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.

 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


"""