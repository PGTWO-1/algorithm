def queen(board, row):
    col = 0
    border = len(board)
    if row >= border:
        print(board)
    while col < border:
        for col in range(border):
            if promissing(board, row, col):
                board[row] = col
                queen(board, row + 1)
        col += 1


def promissing(board, row, col):
    i = 0
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


if __name__ == '__main__':
    n = int(input("Please the size of chessboard: "))
    board = [0 for i in range(n)]
    queen(board, 0)
