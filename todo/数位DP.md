
### 题单
| 题目 | 状态 | 题解 |
| --- | --- | --- |
| [233. 数字 1 的个数](https://leetcode.cn/problems/number-of-digit-one/)   |  | |
|[面试题 17.06. 2出现的次数](https://leetcode.cn/problems/number-of-2s-in-range-lcci/)  |||
|[357. 统计各位数字都不同的数字个数](https://leetcode.cn/problems/count-numbers-with-unique-digits/)  |||
|[600. 不含连续1的非负整数](https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/)  |||
|[902. 最大为 N 的数字组合](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/) |||
|[1012. 至少有 1 位重复的数字](https://leetcode.cn/problems/numbers-with-repeated-digits/)  |||
|[1067. 范围内的数字计数](https://leetcode.cn/problems/digit-count-in-range/)  |||
|[1397. 找到所有好字符串](https://leetcode.cn/problems/find-all-good-strings/)  |||


### 模板
```python
def count_special_numbers(n: int) -> int:
    s = str(n)

    @lru_cache(None)
    def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
        if i == len(s):
            return int(is_num)
        res = 0
        if not is_num:  # 跳过当前数位，相当于填 0
            res = f(i + 1, mask, False, False)
        up = int(s[i]) if is_limit else 9
        for d in range(0 if is_num else 1, up + 1):  # 枚举要填入的数字 d
            if mask >> d & 1 == 0:  # d 不在 mask 中
                res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
        return res
```
题解讲解：[【【力扣周赛 306】数位 DP  | LeetCode 算法刷题】 ](https://www.bilibili.com/video/BV1rS4y1s721?share_source=copy_web&vd_source=d0c4c77f2a523fd642e534d5a9456525)

### 经验总结






 





