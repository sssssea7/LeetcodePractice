# https://leetcode.com/problems/flood-fill/description/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        Q = [(sr, sc)]
        source_color = image[sr][sc]
        if source_color==color:
            return image
        while Q:
            x, y = Q.pop(0)
            image[x][y] = color
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0<=x+dx<n and 0<=y+dy<m and image[x+dx][y+dy] == source_color:
                    image[x+dx][y+dy] = color
                    Q.append((x+dx, y+dy))
        return image