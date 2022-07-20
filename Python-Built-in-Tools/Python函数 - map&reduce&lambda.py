"""
Python中的map和reduce函数简介:
https://blog.csdn.net/qdPython/article/details/115462821
"""

from functools import reduce

if __name__ == '__main__':
    nums = [1, 2, 3, 2, 1]
    print(reduce(lambda x, y: x ^ y, nums))
