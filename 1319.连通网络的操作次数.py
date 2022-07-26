#
# @lc app=leetcode.cn id=1319 lang=python3
#
# [1319] 连通网络的操作次数
# 分析：实质是分析树（or 子图）的数量，当网线数量足够时，答案是树的总数 - 1
# 算法过程：先将连接关系 connections 转换成 dfs 需要的邻接表，再深度优先遍历

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 图论最小生成树基本定理
        if len(connections) < n - 1:
            return -1

        adj = defaultdict(list)
        for i, j in connections:
            adj[i].append(j)
            adj[j].append(i)
        visited = [False] * n

        def dfs(x):
            visited[x] = True
            for y in adj[x]:
                if not visited[y]:
                    dfs(y)

        ans = 0
        for k in range(n):
            if not visited[k]:
                dfs(k)
                ans += 1
        return ans - 1

# @lc code=end
