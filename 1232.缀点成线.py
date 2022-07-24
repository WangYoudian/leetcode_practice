#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#
# https://leetcode.cn/problems/check-if-it-is-a-straight-line/description/
#
# algorithms
# Easy (46.33%)
# Likes:    117
# Dislikes: 0
# Total Accepted:    41K
# Total Submissions: 88.6K
# Testcase Example:  '[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]'
#
# 给定一个数组 coordinates ，其中 coordinates[i] = [x, y] ， [x, y] 表示横坐标为 x、纵坐标为 y
# 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates 中不含重复的点
# 
# 
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True

        def check(x1, y1, x2, y2):
            # 将第一个点视为坐标原点，则12向量与13向量共线
            if x1 == x2 == y1 == y2 == 0:
                return True
            # xi和yi中两个都为0
            elif (x1 == 0 and x2 == 0) or (y1 == 0 and y2 == 0):
                return True
            # xi和yi中只有一个为0
            elif x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0:
                return False
            # 到这里，x和y中都没有0
            else:
                return y1 / y2 == x1 / x2

        v11 = coordinates[1][0] - coordinates[0][0]
        v12 = coordinates[1][1] - coordinates[0][1]
        for i in range(2, n):
            v21 = coordinates[i][0] - coordinates[0][0]
            v22 = coordinates[i][1] - coordinates[0][1]
            if not check(v11, v12, v21, v22):
                return False
        return True


# @lc code=end

