#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
# dfs算法分析：从0开始搜索，循环遍历到n-1，则返回（归）
#       反之，继续搜索节点的后续节点列表（空列表自然退出）
from collections import deque
from functools import lru_cache

# @lc code=start
from typing import List


class Solution:
    # dfs
    # def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    #     n = len(graph)

    #     @lru_cache(None)
    #     def dfs(x):
    #         if x == n - 1:
    #             return [[n-1]]
    #         res = []
    #         for i in graph[x]:
    #             for path in dfs(i):
    #                 res.append([x] + path)
    #         return res
    #     return dfs(0)

    # bfs
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = deque([[0]])
        ans = []
        while q:
            path = q.popleft()
            # 路径符合要求，直接返回
            if path[-1] == n - 1:
                ans.append(path)
            # 搜索下一个
            for nxt in graph[path[-1]]:
                q.append(path + [nxt])
        return ans

# @lc code=end
