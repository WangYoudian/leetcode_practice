#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
# 目标：时间复杂度 O(m + n) ，空间复杂度 O(1) 

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 双指针方法，方法一可以开辟 m+n 空间，将 nums1 和 nums2 进行归并
        # 方法二：由于需要对 nums1 进行 in-place 修改，在方法一种，遍历的同时
        #   没有复制到 nums1 ，而是到新空间的原因是：直接复制到 nums1 中会覆盖 nums1 之后的元素
        #   若是从 nums1 的最后面开始替换，则不存在值的覆盖问题
        p1, p2 = m - 1, n - 1
        # 注：p3 的值
        p3 = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p3 -= 1
                p1 -= 1
            else:
                nums1[p3] = nums2[p2]
                p3 -= 1
                p2 -= 1
        # p1 为 0 ，表示 nums1 全部移到尾部，或者 nums1 本身长度为 0 
        if p1 == -1:
            # p3+1 的原因是 range 表示的范围前闭后开
            for i in range(p3 + 1):
                nums1[i] = nums2[i]
        # p2 == 0 ， nums1 已经是最终状态

# @lc code=end

