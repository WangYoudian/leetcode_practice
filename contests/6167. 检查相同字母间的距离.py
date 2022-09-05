from collections import defaultdict
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        char_dict = defaultdict(list)
        for i, char in enumerate(s):
            char_dict[char].append(i)
        for key, ds in char_dict.items():
            if ds[1] - ds[0] - 1 != distance[ord(key) - ord('a')]:
                return False
        return True
