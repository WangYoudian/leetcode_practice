#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        cnt = 0
        diff = high - low
        if diff % 2 == 1:
            cnt += diff // 2 + 1
        else:
            if high % 2 == 0:
                cnt += diff // 2
            else:
                cnt += diff // 2 + 1
        
        return cnt
# @lc code=end

