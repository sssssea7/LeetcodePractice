# https://leetcode.com/problems/snakes-and-ladders/description/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get_position(square):
            row_from_bottom, offset = divmod(square - 1, n)
            row = n - 1 - row_from_bottom
            if row_from_bottom % 2 == 0:
                col = offset
            else:
                col = n - 1 - offset
            return row, col
        
        n = len(board)
        Q = deque([1])
        seen = {1}
        step = 0
        while Q:
            for _ in range(len(Q)):
                curr = Q.popleft()
                if curr==n**2:
                    return step
                for next_square in range(curr+1, min(curr+6, n**2)+1):
                    new_r, new_c = get_position(next_square)
                    if board[new_r][new_c] != -1:
                        destination = board[new_r][new_c]
                    else:
                        destination = next_square
                    if destination not in seen:
                        seen.add(destination)
                        Q.append(destination)
            step += 1
        return -1