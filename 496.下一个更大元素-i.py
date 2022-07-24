#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    # 模拟
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     n = len(nums1)

    #     def find_next_greater(x):
    #         loc = 0
    #         for i, value in enumerate(nums2):
    #             if value == x:
    #                 loc = i
    #                 break
    #         for j in range(loc+1, len(nums2)):
    #             if nums2[j] > x:
    #                 return nums2[j]
    #         return -1

    #     ans = []
    #     for num in nums1:
    #         ans.append(find_next_greater(num))
    #     return ans

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 对nums2进行预处理
        pre = {}

        for i, value in enumerate(nums2):
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    pre[nums2[i]] = nums2[j]
                    break
            if len(pre) < i + 1:
                pre[nums2[i]] = -1
        ans = []
        for num in nums1:
            # num一定在nums2中，必然命中pre[num]
            ans.append(pre[num])
        return ans

# @lc code=end

