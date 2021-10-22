class Solution:
    def frequencySort(self, s: str) -> str:
        arr = []
        for k, v in Counter(s).items():
            arr.append([k, v])
        arr = sorted(arr, key=lambda x:-x[1])
        ans = ""
        for i in range(len(arr)):
            ans += arr[i][0]*arr[i][1]
        return ans