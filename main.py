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


def getEmptyIndices(board):
    empty_indices = []

    for row_index in range(len(board)):
        for column_index in range(len(board[row_index])):
            if board[row_index][column_index] == 0:
                empty_indices.append([row_index, column_index])

    return empty_indices


def getRow(board, row_index):
    return board[row_index]


def getColumn(board, column_index):
    column = []

    for row_index in range(len(board)):
        column.append(board[row_index][column_index])

    return column


def getSquare(board, row_index, column_index):
    square = []

    row_start = int(row_index / 3) * 3
    column_start = int(column_index / 3) * 3

    for row in range(row_start, row_start + 3):
        for column in range(column_start, column_start + 3):
            square.append(board[row][column])

    return square


def checkRow(board, row_index, number):
    if number not in getRow(board, row_index):
        return True
    return False


def checkColumn(board, column_index, number):
    if number not in getColumn(board, column_index):
        return True
    return False


def checkSquare(board, row_index, column_index, number):
    if number not in getSquare(board, row_index, column_index):
        return True
    return False


def check(board, row_index, column_index, number):
    if checkRow(board, row_index, number) and checkColumn(board, column_index, number) and checkSquare(board, row_index,
                                                                                                       column_index,
                                                                                                       number):
        return True
    return False


def getMissingNumbers(board, row_index, column_index):
    missing_numbers = []
    for number in range(1, 10):
        if check(board, row_index, column_index, number):
            missing_numbers.append(number)
    return missing_numbers


def makeNotes(board, empty_indices):
    notes = []
    possibilities = []

    for empty_index in empty_indices:
        row_index = empty_index[0]
        column_index = empty_index[1]
        missing_numbers = getMissingNumbers(board, row_index, column_index)
        notes.append(missing_numbers)
        possibilities.append(len(missing_numbers))

    return notes, possibilities


def solveBoard(board):
    empty_indices = getEmptyIndices(board)
    notes, possibilities = makeNotes(board, empty_indices)

    while min(possibilities) == 1:
        note_index = possibilities.index(1)
        index = empty_indices[note_index]
        row_index = index[0]
        column_index = index[1]
        board[row_index][column_index] = notes[note_index][0]
        del empty_indices[note_index]
        notes, possibilities = makeNotes(board, empty_indices)
        if not possibilities:
            break

    if possibilities:
        print('Not fully solved yet.')

    # print(empty)
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

    # Solve the board
    solveBoard(board)

    # Display the solved board
    print('\nThe solved sudoku board:')
    printBoard(board)
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
