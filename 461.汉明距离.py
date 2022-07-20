#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 若二进制位不同，则该位异或为1，否则为0
        s = x ^ y
        cnt = 0
        # 使用Boyer Kenighan算法统计1的个数
        while s > 0:
            s &= s - 1
            cnt +=  1
        return cnt
        
        
# @lc code=end

