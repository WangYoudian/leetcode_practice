#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
# 分析：26进制

# @lc code=start
import string


class Solution:
    def convertToTitle(self, column_number: int) -> str:
        arr = string.ascii_uppercase
        ans = []
        while column_number > 0:
            rest = (column_number - 1) % 26
            ans.insert(0, arr[rest])
            # 701=26*26+25，表示为ZY，num-1为实际26进制下标值
            column_number = (column_number - 1) // 26
        return ''.join(ans)

# @lc code=end

