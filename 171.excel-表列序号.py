#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, column_title: str) -> int:
        res = []
        for c in column_title:
            res.append(ord(c) - ord('A') + 1)
        ans = 0
        for num in res:
            ans = ans * 26 + num
        return ans
# @lc code=end

