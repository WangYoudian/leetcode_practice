#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
# 双指针

# @lc code=start
class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     zero = 0  # records the position of "0"
    #     for i in range(len(nums)):
    #         if nums[i] != 0:
    #             nums[i], nums[zero] = nums[zero], nums[i]
    #             zero += 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = 0
        cnt = 0
        for i in range(n):
            if nums[i] == 0:
                cnt += 1
            else:
                nums[p] = nums[i]
                p += 1
        for i in range(n - cnt, n):
            nums[i] = 0

# @lc code=end
'''
评价：第一种实现相较第二种更优，使用 zero 指针记录下了零在 nums 中间的位置
中间会形成一段连续的 0 ，随着下标 i 的推移，将后面的非零元素与 0 序列的开头交换
在遍历的同时，“实时”进行非零的复制，复杂度为固定的 O(n) 。第二种最差时间复杂度为 O(2n)
'''
