class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def no_to_pos(no):
            row = (no - 1) // length
            col = (no - 1) % length
            if row % 2:
                col = length - 1 - col
            return (row, col)

        q = []
        vis = set()
        q.append((1, 0))
        while q:
            square, moves = q[0]
            del q[0]
            for dice in range(1, 7):
                next_square = square + dice
                r, c = no_to_pos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == length * length:
                    return moves + 1
                if next_square not in vis:
                    vis.add(next_square)
                    q.append((next_square, moves + 1))
        return -1
