"""
Python中的map和reduce函数简介:
https://blog.csdn.net/qdPython/article/details/115462821
"""

from functools import reduce

if __name__ == '__main__':
    nums = [1, 2, 3, 2, 1]
    print(reduce(lambda x, y: x ^ y, nums))

    arr = list(map(int, "1 2 3 4".split(" ")))
    print(arr)

    a = [4, 1, 2]
    b = [-2, -1, 3]
    # 根据b中对应位置数据对zip后的列表排序
    # 注： 与 zip 相反，zip(*) 可理解为解压
    c = sorted(list(zip(a, b)), key=lambda x: x[1], reverse=True)
    print(c)
    a1, b1 = zip(*zip(a, b))
    print(list(a1), list(b1))
