#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
# 模拟：存在题述矩阵，输入字符串将呈现 Z 字形，即纵向填充
#   输出时，则是横向输出。
# 一种思路是，根据 numRows 计算 s 中有哪些属于第 1...n 行
# 这种算法比按照 s 原顺序粘贴 numRows 个字符序列复杂的多
# 因此，通过 一个行号指针 row 和 一个方向指针 step 模拟输入字符的填充过程

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        lines = [""] * numRows
        row, step = 0, 1
        for c in s:
            lines[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            # 中间情形，字符序列上下走向不变， step 不做变更
            row += step
        return "".join(lines)

# @lc code=end

