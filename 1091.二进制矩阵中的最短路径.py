#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
# bfs过程分析：路径长度计数变量dis，每将队列中上一轮元素遍历完
#       dis自增1。直到抵达grid[n-1][n-1]，返回dis+1
#       由于是求最短路径，为了避免重复搜索，将舍弃掉已经访问过的节点
from collections import deque

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        n = len(grid)
        if grid[0][0] != 0:
            return -1
        if n == 1:
            return 1
        q = deque()
        q.appendleft((0, 0))
        visited = set()
        # grid[0][0]计入长度
        dis = 1
        while q:
            # 轮次分界计数器
            for _ in range(len(q)):
                # 节点从右边出队
                x, y = q.pop()
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and \
                        (nx, ny) not in visited:
                        # 路径搜索成功，直接返回
                        if nx == n -1 and ny == n -1:
                            return dis + 1
                        q.appendleft((nx, ny))
                        visited.add((nx, ny))
            dis += 1
        # 不存在合法路径
        return -1


# @lc code=end

