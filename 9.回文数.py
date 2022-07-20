#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        for i in range(n):
            if s[i] != s[n-i-1]:
                return False
        return True
# @lc code=end

