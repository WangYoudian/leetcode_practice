#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
from hashlib import new
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(image), len(image[0])
        init = image[sr][sc]
        visited = [[0]*n for _ in range(m)]

        def dfs(x, y):
            image[x][y] = color
            visited[x][y] = 1
            for d in DIR:
                dx, dy = d[0], d[1]
                new_row, new_col = x + dx, y + dy
                # 像素值判断，必须与初始值相等
                if 0 <= new_row < m and 0 <= new_col < n and \
                        image[new_row][new_col] == init and \
                        visited[new_row][new_col] != 1:
                    # image[new_row][new_col] = color
                    dfs(new_row, new_col)

        dfs(sr, sc)
        return image  

# @lc code=end

