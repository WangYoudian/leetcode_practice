#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        adder1 = int('0b' + a, 2)
        adder2 = int('0b' + b, 2)
        ans = bin(adder1 + adder2)[2:]
        return ans

# @lc code=end

