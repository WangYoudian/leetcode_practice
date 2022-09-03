from functools import lru_cache


def count_special_numbers(n: int) -> int:
    s = str(n)

    @lru_cache(None)
    def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
        if i == len(s):
            return int(is_num)
        res = 0
        if not is_num:  # 可以跳过当前数位
            res = f(i + 1, mask, False, False)
        up = int(s[i]) if is_limit else 9
        for d in range(0 if is_num else 1, up + 1):  # 枚举要填入的数字 d
            if mask >> d & 1 == 0:  # d 不在 mask 中
                res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
        return res

    return f(0, 0, True, False)


def start():
    print(count_special_numbers(n))


if __name__ == '__main__':
    n = 20
    start()
