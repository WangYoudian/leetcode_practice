#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        diff = []
        for i in range(n):
            if s1[i] != s2[i]:
                diff.append(i)
        if not diff:
            return True
        if len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and\
            s1[diff[1]] == s2[diff[0]]:
            return True
        return False
# @lc code=end

