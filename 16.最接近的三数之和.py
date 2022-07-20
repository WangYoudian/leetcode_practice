#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
# 『双指针』
# 基本思路：

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        # 不是10**4，避免中间有出现误差项（10**4有一个用例fail）
        best = 10**7

        for first in range(n -2):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            second, third = first + 1, n -1
            while second < third:
                s = nums[first]+ nums[second]+nums[third]
                if abs(s- target) < abs(best -target):
                    best= s
                if s < target:
                    second += 1
                    # right_most = third -1
                    # while second < right_most and nums[second] == nums[second+1]:
                    #     second += 1
                elif s > target:
                    third -= 1
                    # left_most = second + 1
                    # while third > left_most and nums[third] == nums[third-1]:
                    #     third -= 1
                else:
                    return target
        return best

# @lc code=end

