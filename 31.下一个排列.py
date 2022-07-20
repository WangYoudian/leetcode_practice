#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
# C++中next_permutation实现采用的方法
# 两遍扫描
# 先从后往前找到一个『较小数』，再从后往前搜索第一个大于『较小数』的『较大数』
# 最后交换二者位置，同时，反转『较大数』后面的序列，从降序变为升序

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        x, y = n - 1, n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                x = i
                break
        for j in range(n - 1, x, -1):
            if nums[j] > nums[x]:
                y = j
                break
        nums[x], nums[y] = nums[y], nums[x]
        # x在正常情况下是<n-1，若为n-1，则序列已经降序，整体换为升序
        # 以x作为待反转区间的起始下标
        if x == n - 1:
            x = 0
        else:
            x += 1

        # 修改『较小值』后面降序序列为升序。注意下标位置的运算
        for k in range(x, (n - x) // 2 + x):
            nums[k], nums[n - 1 - k + x] = nums[n - 1 - k + x], nums[k]


# @lc code=end
# 注：本质上，这种问题就是在处理逆序数
# 下一个序列就是逆序数大1的序列，因此首先需要找最小可以交换的数
# 存在一个『较大数』和『较小数』，且二者极为接近
# 模拟[4,5,2,6,3,1]，经过运算得到[4,5,3,1,2,6]
# 可以看出，整个序列可以看做左边乱序，右边降序两个序列组成，
# 每次从后往前找，找到第一个打破降序的数字，用降序序列中刚好大于它的替代
# 同时为了降低二者交换对整体逆序数的增长，将原先降序的序列调整为升序
# 但是调整之后逆序数整体上仍然是增长
