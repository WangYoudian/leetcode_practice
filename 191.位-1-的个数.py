#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 特殊的算法
        cnt = 0
        while n > 0:
            n &= n -1
            cnt += 1
        return cnt
        
# @lc code=end

