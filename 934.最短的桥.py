#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#
# 思路：先使用dfs分别找到两座岛（坐标的列表），然后从一座岛开始bfs，
# 每一次bfs，都使得这座岛扩散一格，直到与另一组岛相遇，bfs的次数就是ans

# @lc code=start
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        def dfs(x, y):
            visited[x][y] = 1
            area = [(x, y)]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and\
                    visited[nx][ny] == 0:
                    area.extend(dfs(nx, ny))
            return area
        
        islands = []
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    islands.append(dfs(i, j))
        
        # 题目保证了存在两座岛，这里省略对islands的校验
        q = deque()
        ia, ib = islands[0], islands[1]
        for p in ia:
            q.append(p)
        ans = 0
        while q:
            ps = len(q)
            ans += 1
            for _ in range(ps):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in ib:
                        # 根据示例，返回结果是岛屿中间 0 的个数
                        return ans - 1
                    elif 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        q.append((nx, ny))
                        # 模拟岛屿膨胀
                        grid[nx][ny] = 1

# @lc code=end
