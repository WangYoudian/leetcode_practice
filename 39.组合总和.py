#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        def dfs(nums, target_, path_, res):
            if target_ < 0:
                return
            if target_ == 0:
                res.append(path_)
                return
            for index in range(len(nums)):
                dfs(nums[index:], target_ - nums[index], path_ + [nums[index]], res)

        ans = []
        path = []
        # candidates.sort()
        dfs(candidates, target, path, ans)
        return ans

# @lc code=end
