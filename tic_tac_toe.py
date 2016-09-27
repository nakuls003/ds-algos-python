class TicTacToe:
    """A class simulating a game of tic tac toe"""

    def __init__(self):
        self._board = [[' ']*3 for _ in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position. Try again!")
        if self._board[i][j] != ' ':
            raise ValueError("Board position already occupied!")
        if self.winner() is not None:
            raise ValueError("Game is already complete!")
        self._board[i][j] = self._player
        self._player = 'O' if self._player == 'X' else 'X'

    def _is_win(self, p):
        b = self._board
        return (p == b[0][0] == b[0][1] == b[0][2] or
                p == b[1][0] == b[1][1] == b[1][2] or
                p == b[2][0] == b[2][1] == b[2][2] or
                p == b[0][0] == b[1][0] == b[2][0] or
                p == b[0][1] == b[1][1] == b[2][1] or
                p == b[0][2] == b[1][2] == b[2][2] or
                p == b[0][0] == b[1][1] == b[2][2] or
                p == b[0][2] == b[1][1] == b[2][0])

    def winner(self):
        for player in 'XO':
            if self._is_win(player):
                return player
        return None

    def __str__(self):
        rows = ['|'.join(self._board[i]) for i in range(3)]
        return "\n-----\n".join(rows)
