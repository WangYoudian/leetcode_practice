#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
# 『双指针』

# @lc code=start
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 4:
            return []

        ans = []

        last_three_sum = nums[n-1] + nums[n-2] + nums[n-3]
        last_tow_sum = nums[n-1] + nums[n-2]
        for first in range(n-3):
            # a避免取重
            if first > 0 and nums[first] == nums[first-1]:
                continue
            # 若a后紧跟的3个数之和大于target，则后面3个数无论怎么取，都大于target
            if nums[first] + nums[first+1] + nums[first+2] + nums[first+3] > target:
                break
            # 若a与最大的三个数之和小于target，则当前a过小，跳到下一个候选值
            if nums[first] + last_three_sum < target:
                continue
            for second in range(first+1, n-2):
                # b可能等于a，但b的候选值之间，避免取重
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                if nums[first] + nums[second] + nums[second+1] + nums[second+2] > target:
                    break
                if nums[first]+nums[second] + last_tow_sum < target:
                    continue

                left, right = second + 1, n - 1
                new_target = target - nums[first] - nums[second]
                while left < right:
                    two_sum =nums[left] + nums[right]
                    if  two_sum < new_target:
                        left += 1
                    elif two_sum > new_target:
                        right -= 1
                    else:
                        ans.append([nums[first], nums[second], nums[left], nums[right]])
                        # 去重+左右指针各自变化1个位置
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
        return ans
         
# @lc code=end
# 总结：类似的数组中取不重复子集，可以考虑排序。且在循环中可以注意两点：
# 1. 每一种循环枚举到的下标必须大于上一重循环枚举到的下标；
# 2. 同一重循环中，如果当前元素与上一个元素相同，则跳过当前元素。
