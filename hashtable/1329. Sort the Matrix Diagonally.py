class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ht = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ht[i-j].append(mat[i][j])
        for k, v in ht.items():
            ht[k] = sorted(ht[k])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = ht[i-j].pop(0)
        return mat