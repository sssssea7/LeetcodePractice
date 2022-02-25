class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        for x, y in zip_longest(v1.split("."), v2.split("."), fillvalue="0"):
            if int(x) > int(y): return 1
            elif int(x) < int(y): return -1
        return 0