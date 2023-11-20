class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = len("".join(garbage))
        G_s, M_s, P_s = 0, 0, 0
        Gf, Mf, Pf = True, True, True
        for i in range(len(garbage)-1, -1, -1):
            if Gf and "G" in garbage[i]: 
                G_idx = i
                G_s = sum(travel[0:G_idx])
                Gf = False
            if Mf and "M" in garbage[i]: 
                M_idx = i
                M_s = sum(travel[0:M_idx])
                Mf = False
            if Pf and "P" in garbage[i]: 
                P_idx = i
                P_s = sum(travel[0:P_idx])
                Pf = False
        ans += G_s + M_s + P_s
        return ans