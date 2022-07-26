#
# @lc app=leetcode.cn id=1926 lang=python3
#
# [1926] 迷宫中离入口最近的出口
# 分析：BFS
# 对于走过的路，从 '.' 设置为 '+'

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque([tuple(entrance)])
        ans = 0
        while q:
            ls = len(q)
            ans += 1
            for _ in range(ls):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    # x, y 即为边界点
                    if nx == m or nx < 0 or ny == n or ny < 0:
                        # 按照题意， entrance 格子不算出口
                        if (x, y) != tuple(entrance):
                            return ans - 1
                        
                    # 在矩阵范围内
                    elif maze[nx][ny] == '.':
                        q.append((nx, ny))
                        maze[nx][ny] = '+'
        # 走不出迷宫
        return -1

# @lc code=end

