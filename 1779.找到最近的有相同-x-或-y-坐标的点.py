#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

# @lc code=start

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = []
        for i, d in enumerate(points):
            dx, dy = d[0], d[1]
            if dx == x or dy == y:
                distance = abs(x -dx) + abs(y -dy)
                result.append([i, distance])
        # 根据distance升序排序，返回最小distance的下标
        result.sort(key=lambda x: x[1])
        if not result:
            return -1
        return result[0][0]

# @lc code=end

