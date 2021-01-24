import collections
class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        cnt = collections.Counter(s[:len(p)])
        t = collections.Counter(p)
        for i in range(len(s)-len(p)):
            if cnt == t: ans.append(i)
            cnt[s[i]] -= 1
            if not cnt[s[i]]: del cnt[s[i]]
            cnt[s[i+len(p)]] +=1
        if cnt==t: ans.append(i+1)
        return ans