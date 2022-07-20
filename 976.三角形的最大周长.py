#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
from audioop import reverse


class Solution:
    # 三重循环+剪枝判断（贪心策略）
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        ans = 0

        for i in range(n-2):
            a = nums[i]
            if nums[i+1] + nums[i+2] > a:
                ans = max(ans, a + nums[i+1] + nums[i+2])
                continue
            if nums[i+1] + nums[i+2] < a:
                continue
            for j in range(i+1, n-1):
                b = nums[j]
                if nums[j+1] < a - b:
                    continue
                if nums[j+1] + b > a:
                    ans = max(ans, a + b + nums[j+1])
                    continue
                for k in range(j+1, n):
                    c = nums[k]
                    if c + b > a:
                        ans = max(ans, a + b + c)
                        break
        return ans


# @lc code=end

