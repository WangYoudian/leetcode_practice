#
# @lc app=leetcode.cn id=1887 lang=python3
#
# [1887] 使数组元素相等的减少操作次数
# 等价：为了使得nums中所有元素相等，需要将nums中任意元素都变成nums
#       中的最小值；任意元素，需要的操作数是严格小于它的不同值的数量
# 为了简化，先对数组进行排序。然后一次遍历（***）

# @lc code=start
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # nums从小到大排列
        nums.sort()
        n = len(nums)
        if n < 2:
            return 0
        
        ans = 0
        cnt = 0
        for i in range(1, n):
            # cnt记录从最小值（本身不计），往后递增的不同数值的种数
            # cnt的值等于相应的nums[i]需要操作的次数
            if nums[i] != nums[i-1]:
                cnt += 1
            ans += cnt
        return ans

# @lc code=end

