#
# @lc app=leetcode.cn id=1306 lang=python3
#
# [1306] 跳跃游戏 III
# 分析：题意为判断元素 0 的可达性
# 采用 dfs ，每次都将处在数组合法下标中，且未被访问到的元素递归
# 对于已经访问过的，忽略

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n

        def dfs(x):
            if arr[x] == 0:
                return True
            tag = False
            cands = [x + arr[x], x - arr[x]]
            for cand in cands:
                if 0 <= cand < n and visited[cand] is False:
                    visited[cand] = True
                    tag |= dfs(cand)
            return tag
        
        return dfs(start)

# @lc code=end

