#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums:
            return ans
        p = 0
        cnt = 0
        while p < len(nums) - 1:
            if nums[p] < nums[p + 1] - 1:
                if cnt > 0:
                    ans.append("%s->%s" %(str(nums[p - cnt]), str(nums[p])))
                else:
                    ans.append(str(nums[p]))
                cnt = 0
                p += 1
            # num[p] 和 nums[p+1] 连续
            else:
                cnt += 1
                p += 1
        # 处理最后一组范围
        if cnt > 0:
            ans.append("%s->%s" % (str(nums[p - cnt]), str(nums[p])))
        else:
            ans.append(str(nums[p]))
        return ans
# @lc code=end

