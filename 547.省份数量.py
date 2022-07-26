#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
from typing import List


class Solution:
    def findCircleNum(self, adj_matrix: List[List[int]]) -> int:
        """

        :param adj_matrix: 邻接矩阵
        :return:
        """
        n = len(adj_matrix)
        # seen 记录已经访问过的省份
        seen = set()

        def dfs(p):
            seen.add(p)
            for q, adj in enumerate(adj_matrix[p]):
                if adj and q not in seen:
                    dfs(q)

        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans


# @lc code=end

