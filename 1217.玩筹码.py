#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0
        for p in position:
            if p % 2 == 1:
                odd += 1
            else:
                even += 1
        return min(odd, even)
# @lc code=end

