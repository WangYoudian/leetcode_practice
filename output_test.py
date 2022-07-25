from typing import List
# -----------------------------------------------------------
# @lc code=start

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        max_odd_length = n if n % 2 == 1 else n - 1
        ans = 0
        for j in range(1, max_odd_length+1, 2):
            # sub_sum 是首个长度为 j 的数组的和，后续使用滑动窗口维护这个和
            sub_sum = sum(arr[:j])
            # partial 是以 j 为数组长度的所有子数组的和的和
            partial = sub_sum
            for i in range(n - j):
                sub_sum = sub_sum + arr[i + j] - arr[i]
                partial += sub_sum
            ans += partial
        return ans

# @lc code=end
# ------------------------------------------------------------------------


if __name__ == '__main__':
    solution = Solution()
    # input data here
    arr = [1, 4, 2, 5, 3]
    # get or print result from solution.<function>
    print(solution.sumOddLengthSubarrays(arr))
