#
# @lc app=leetcode.cn id=1376 lang=python3
#
# [1376] 通知所有员工所需的时间
# 分析：DFS ，自底向上

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_cost: List[int]) -> int:
        """

        :param n: 员工数量
        :param head_id: 公司总负责人ID
        :param manager: 人员架构
        :param inform_cost: 通知耗时，树节点间路径的权值
        :return:
        """
        @lru_cache(None)
        def dfs(i):
            # 由于叶子节点的耗时是 0 ，因此 dfs 结果需要加上 manager[i] 的 inform 开销
            # 而不是 i 的开销
            if i == head_id or manager[i] == head_id:
                return inform_cost[head_id]
            return dfs(manager[i]) + inform_cost[manager[i]]
        
        ans = 0
        for j in range(n):
            cost = dfs(j)
            ans = max(ans, cost)
        return ans

# @lc code=end

