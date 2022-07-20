#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
# 使用BFS，反向求解，从陆地出发广度优先遍历，直到最远的海域
from collections import deque


# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.appendleft((i, j))
        # 若全部为海洋或者陆地
        if len(q) == 0 or len(q) == n**2:
            return -1
        # 由于采用了逆向的模拟，队列遍历的轮次实际上应等于所求答案减1
        # 因此ans初始化为-1
        ans = -1
        while q:
            for _ in range(len(q)):
                x, y = q.pop()
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        q.appendleft((nx, ny))
                        # 已经访问过进行标记
                        grid[nx][ny] = -1
            ans += 1
        return ans

# @lc code=end
# 题解：https://leetcode.cn/problems/as-far-from-land-as-possible/solution/python-tu-jie-chao-jian-dan-de-bfs1162-di-tu-fen-x/

