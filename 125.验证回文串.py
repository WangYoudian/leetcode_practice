#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for c in s:
            if c.isdigit() or c.isalpha():
                # 大写字母要转小写
                if c.isalpha():
                    c = c.lower()
                st += c
        n = len(st)
        for i in range(n):
            if st[i] != st[n - i - 1]:
                return False
        return True
# @lc code=end

