class Solution:
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        left, right = 0, len(s)-1 
        while left < right:
            while left<right and s[left] not in "aeiouAEIOU":
                left += 1
            while left<right and s[right] not in "aeiouAEIOU":
                right -= 1
            slist[left], slist[right] = slist[right], slist[left]
            left+=1
            right-=1
        s = "".join(slist)
        return s