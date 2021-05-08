class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = [min(r) for r in matrix]
        max_col = [max(c) for c in list(zip(*matrix))]  # extract col of a matrix
        return set(min_row).intersection(max_col)      # find common elements of two arrays