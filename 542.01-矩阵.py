#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
# 分析：BFS，从 0 出发，到每一个 1 的路径长度，即为每一个格子为 1 到最近 0 的距离


# @lc code=start
from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len((mat[0]))
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))

        ans = [[0] * n for _ in range(m)]
        cnt = 0
        while q:
            ps = len(q)
            cnt += 1
            for _ in range(ps):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == 1:
                        q.append((nx, ny))
                        mat[nx][ny] = 0
                        ans[nx][ny] = cnt
        return ans

# @lc code=end
"""
想象力：https://assets.leetcode-cn.com/solution-static/542/fig1.PNG
我们需要对于每一个 1 找到离它最近的 0。如果只有一个 0 的话，我们从这个 0 开始广度优先搜索就可以完成任务了；
但在实际的题目中，我们会有不止一个 0。我们会想，要是我们可以把这些 0 看成一个整体好了。有了这样的想法，
我们可以添加一个「超级零」，它与矩阵中所有的 0 相连，这样的话，任意一个 1 到它最近的 0 的距离，
会等于这个 1 到「超级零」的距离减去一。由于我们只有一个「超级零」，我们就以它为起点进行广度优先搜索。
这个「超级零」只和矩阵中的 0 相连，所以在广度优先搜索的第一步中，「超级零」会被弹出队列，而所有的 0 会被加入队列，
它们到「超级零」的距离为 1。这就等价于：一开始我们就将所有的 0 加入队列，它们的初始距离为 0。
这样以来，在广度优先搜索的过程中，我们每遇到一个 1，就得到了它到「超级零」的距离减去一，也就是 这个 1 到最近的 0 的距离。

拓展：
熟悉「最短路」的读者应该知道，我们所说的「超级零」实际上就是一个「超级源点」。
在最短路问题中，如果我们要求多个源点出发的最短路时，一般我们都会建立一个「超级源点」连向所有的源点，
用「超级源点」到终点的最短路等价多个源点到终点的最短路。

"""
