def printBoard(board):
    # Iterate over every row in the board
    for row_index in range(len(board)):
        # Because the idea of this printBoard function is to be generic,
        # only if the length of the board is divisible by 3 should the
        # display have 3 by 3 blocks
        if len(board) % 3 == 0:
            # If the current row is divisible by 3, print a grid-line
            if row_index % 3 == 0:
                print('-' * (len(board) * 3 - 2))

        # Iterate over every column in the row
        for column_index in range(len(board[row_index])):
            if len(board[row_index]) % 3 == 0:
                # If the current column is divisible by 3, print a grid-line
                if column_index % 3 == 0:
                    print('|', end=' ')

            # If the current number in the grid is 0, replace it with a space
            if board[row_index][column_index] == 0:
                print(' ', end=' ')
            else:
                print(board[row_index][column_index], end=' ')

        # At the end of the row, print a grid-line
        if len(board[row_index]) % 3 == 0:
            print('|')
        else:
            print()

    if len(board) % 3 == 0:
        print('-' * (len(board) * 3 - 2))

    return


def main():
    # Get the sudoku board that needs to be solved
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    # Display the board's starting state to the screen
    print('The starting sudoku board:')
    printBoard(board)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
