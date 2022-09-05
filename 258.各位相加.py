#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        while not (0 < num < 10):
            num = sum(list(map(int, list(str(num)))))
        return num
# @lc code=end
