#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#
# 补码的加法运算
# 分析：我们可以将整数 a 和 b 的和，拆分为 a 和 b 的无进位加法结果与进位结果的和。

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Python的实现对整型的位数没有限制，可能导致整型向上溢出，因此要对2^32取余
        MASK1 = 2**32
        # 结果中首位为1，需要将负数补码转为负数，MASK2 MASK3都是补码转换辅助参数
        MASK2 = 2**31
        MASK3 = 2**31 - 1
        # 为什么a、b需要对2^32取余？
        # eg.求 (-12) + (-8)
        # print(bin(-12))
        # print(bin(-12 % (2**32)))
        # -0b1100
        # 0b11111111111111111111111111110100  # 为负数补码
        a %= MASK1
        b %= MASK1
        # 移位加法器
        while b > 0:
            # a+b的进位的值，最终要“加”到a上
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            # b是被加数，进位的值赋给b，继续循环，直到不再产生进位（b = 0）
            b = carry
        # 若结果a为负数，求负数的原码
        if a & MASK2:
            return  ~((a ^ MASK2) ^ MASK3)
        # a为非负数
        else:
            return a

# @lc code=end

