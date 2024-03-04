# Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера

def displayBoard(board):
    print(f"\n {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("-----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("-----------")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")


def printBoardNumbers():
    print("\n 7 | 8 | 9")
    print("-----------")
    print(" 4 | 5 | 6")
    print("-----------")
    print(" 1 | 2 | 3\n")


def checkWinner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[i][col] == player for i in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def isBoardFull(board):
    return all(cell != ' ' for row in board for cell in row)


def getPlayerMove(board, player):
    while True:
        try:
            move = input(f"Игрок {player}, введите номер поля (1-9): ")
            position = int(move) - 1
            row = position // 3
            col = position % 3
            if board[row][col] != ' ' or not 0 <= position <= 8:
                print("Некорректный ход! Попробуйте снова.")
                continue
            return row, col
        except ValueError:
            print("Некорректный ввод! Введите номер поля от 1 до 9.")


def ticTacToe():
    board = [[' ' for i in range(3)] for j in range(3)]
    currentPlayer = 'X'

    print("Добро пожаловать в игру Крестики-нолики!")
    print("Ниже представлена нумерация полей:")
    printBoardNumbers()

    while True:
        row, col = getPlayerMove(board, currentPlayer)
        board[row][col] = currentPlayer

        if checkWinner(board, currentPlayer):
            displayBoard(board)
            print(f"Игрок {currentPlayer} победил!")
            break
        elif isBoardFull(board):
            displayBoard(board)
            print("Ничья! Никто не победил.")
            break
        else:
            displayBoard(board)
            currentPlayer = 'O' if currentPlayer == 'X' else 'X'


if __name__ == "__main__":
    ticTacToe()
