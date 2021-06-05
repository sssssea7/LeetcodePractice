class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()
        for i in range(len(searchWord)):
            s = searchWord[:i+1]
            cand = [p for p in products if p[:i+1]==s]
            ans.append(cand[:3])
        return ans