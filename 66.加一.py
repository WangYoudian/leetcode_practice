#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 加法进位， 这里 i 可以是 0-9 任意的数字
        carry, i = 0, 1
        p = len(digits) - 1
        while p >= 0:
            if digits[p] + i >= 10:
                carry = 1
                i = (digits[p] + i) % 10
                digits[p] = i
                i = carry
                p -= 1
            # 不产生进位，前面 p 个数字照抄，直接返回即可
            else:
                digits[p] = digits[p] + i
                return digits

        # p 一直到 -1 都没有 return ，则原 digits 中都是 9 ，加1位数增加一位
        digits.insert(0, 1)
        return digits


# @lc code=end

