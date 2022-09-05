from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = [0] * len(queries)
        nums_sum = [sum(nums[:i + 1]) for i in range(len(nums))]
        for i in range(len(queries)):
            index = 0
            while nums_sum[index] <= queries[i] and index < len(nums):
                if index == len(nums) - 1:
                    index += 1
                    break
                index += 1
            ans[i] = index
        return ans
