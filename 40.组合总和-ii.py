#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0:
            return []

        def dfs(start, target_, path, res):
            if target_ == 0:
                res.append(path)
                return
            for index in range(start, len(nums)):
                # 去重
                if index > start and nums[index] == nums[index - 1]:
                    continue
                if nums[index] > target_:
                    break
                dfs(index + 1, target_ - nums[index], path + [nums[index]], res)

        ans = []
        nums.sort()
        dfs(0, target, [], ans)
        return ans

# @lc code=end

