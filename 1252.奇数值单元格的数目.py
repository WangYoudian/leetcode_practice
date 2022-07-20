#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
# 算法分析：第一次将产生m+n-1个奇数，此后每次落子，都视为两次操作
# 针对某行+1，针对某列+1
# 因此，分别提取indices中的行与列，以行为例：若有偶数次操作，则对列操作无影响
# 记录奇数次操作过的行（与不同的奇数次操作的列），行与列操作的交点
# 最终的值应为偶数

# @lc code=start
from collections import defaultdict

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for indice in indices:
            rows[indice[0]] += 1
            cols[indice[1]] += 1
        cnt_r = sum([row % 2 for row in rows])
        cnt_c = sum([col % 2 for col in cols])
        return (m - cnt_r) * cnt_c + (n - cnt_c) * cnt_r
            

# @lc code=end

