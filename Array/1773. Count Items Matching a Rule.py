class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        for i in items:
            if ruleKey == "type" and ruleValue == i[0]: ans += 1
            elif ruleKey == "color" and ruleValue == i[1]: ans += 1
            elif ruleKey == "name" and ruleValue == i[2] : ans += 1
        return ans