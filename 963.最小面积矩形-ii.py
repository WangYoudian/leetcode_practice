#
# @lc app=leetcode.cn id=963 lang=python3
#
# [963] 最小面积矩形 II
# 矩形形成的条件，长与宽垂直
# 穷举任意三点（有序），判断是否垂直，若垂直，则推断第四点，在点集中则能形成一个矩形

# @lc code=start
import math
from itertools import permutations


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def dis(vec):
            return math.sqrt(vec[0]**2 + vec[1]**2)

        ans = float("inf")
        # 点集预处理，更快的判断 p4 是否在点集中
        points = set(map(tuple, points))
        for p1, p2, p3 in permutations(points, 3):
            v12 = (p2[0] - p1[0], p2[1] - p1[1])
            v32 = (p2[0] - p3[0], p2[1] - p3[1])
            if v12[0] * v32[0] + v12[1] * v32[1] == 0:
                # 元组赋值
                p4 = p1[0] + p3[0] - p2[0], p1[1] + p3[1] - p2[1]
                if p4 in points:
                    area = dis(v12) * dis(v32)
                    ans = min(ans, area)
        # 若不存在矩形，返回0
        return ans if ans < float("inf") else 0


# @lc code=end

