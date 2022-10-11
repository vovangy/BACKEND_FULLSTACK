
class TicTacGame:

    def __init__(self):
        self.board = []

    def show_board(self):
        print("-------")
        for i in range(9):
            print(f"|{i + 1 if self.board[i] == 0 else self.choose_tictac(i)}",
                  end="")
            if (i + 1) % 3 == 0:
                print("|")
        print("-------")

    def next_tictac(self):
        return sum(self.board) * -1 + (sum(self.board) + 1) % 2

    def validate_input(self, cell):
        try:
            cell = int(cell)
        except ValueError:
            print("Неверный ввод")
            return 0
        result = 1
        if 0 < cell <= 9:
            if self.board[cell - 1] == 0:
                self.board[cell - 1] = self.next_tictac()
            else:
                print(f"Ячейка с номером {cell} занята")
        else:
            result = 0
            print(f"Ячейки с номером {cell} не существует")
        return result

    def start_game(self):
        self.board = [0 for i in range(9)]
        while self.check_winner() == -2:
            self.show_board()
            print("Введите номер ячейки от 1 до 9")
            cell = input()
            self.validate_input(cell)
        self.show_board()
        self.print_winner()

    def check_winner(self):
        result = -2
        for i in range(1, 5):
            for j in range(1, 8):
                if (j - i < 0 or j + i > 8 or (j != 4 and i == 2)):
                    continue
                sum_bd = self.board[j] + self.board[j - i] + self.board[j + i]
                if abs(sum_bd) == 3:
                    result = sum_bd / 3
        if 0 not in self.board and result == -2:
            result = 0
        return result

    def check_cell(self, cell):
        if self.board[cell] == 0:
            result = 0
        else:
            result = 1
        return result

    def choose_tictac(self, cell):
        if self.board[cell] == 1:
            result = "X"
        else:
            result = "O"
        return result

    def print_winner(self):
        if self.check_winner() == 1:
            print("Выйграли Крестики!")
        elif self.check_winner() == 0:
            print("Выйграли Нолики!")
        else:
            print("Ничья!")

    def test_game(self):
        self.board = [0 for i in range(9)]
        i = 0
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while self.check_winner() == -2:
            self.show_board()
            print("Введите номер ячейки от 1 до 9")
            cell = values[i]
            self.validate_input(cell)
            i += 1
        self.show_board()
        self.print_winner()


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
