from dataclasses import dataclass
from functools import reduce
from typing import Optional


@dataclass
class Cell:
    value: int
    drawn: bool


@dataclass
class BingoCard:
    board: list[list[Cell]]
    last_drawn: Optional[int] = None

    def __init__(self, board: list[list[Cell]]) -> None:
        self.board = []
        for r in board:
            row = [Cell(element, False) for element in r]
            self.board.append(row)

    def draw_number(self, number: int) -> None:
        self.last_drawn = number
        for r in self.board:
            for e in r:
                if e.value == number:
                    e.drawn = True
                    return

    def has_bingo(self) -> bool:
        for row in self.board:
            row_statuses = [cell.drawn for cell in row]
            row_bingo = reduce(lambda x, y: x and y, row_statuses)
            if row_bingo:
                return True

        for ind in range(len(self.board[0])):
            col_statuses = [row[ind].drawn for row in self.board]
            col_bingo = reduce(lambda x, y: x and y, col_statuses)
            if col_bingo:
                return True
        return False

    def calculate_score(self) -> int:
        score = 0
        for row in self.board:
            row_val = [cell.value for cell in row if not cell.drawn]
            if row_val:
                score += sum(row_val)

        return score * self.last_drawn


def read_input(filename: str) -> tuple[list[int], list[BingoCard]]:
    with open(filename) as f:
        file = f.read().split("\n\n")
    sequence = list(map(int, file[0].split(",")))

    squares = list(map(lambda square: square.strip().split("\n"), file[1:]))
    boards = []
    for square in squares:
        board = []
        for line in square:
            row = list(map(int, line.strip().split()))
            board.append(row)
        boards.append(BingoCard(board))

    return sequence, boards


def part_one(filename: str) -> int:
    sequence, boards = read_input(filename)
    for num in sequence:
        for board in boards:
            board.draw_number(num)
            if board.has_bingo():
                return board.calculate_score()

    return 0


def part_two(filename: str) -> int:
    sequence, boards = read_input(filename)
    for num in sequence:
        for board in boards:
            board.draw_number(num)
            if board.has_bingo():
                if len(boards) != 1:
                    boards.remove(board)
                else:
                    return board.calculate_score()

    return 0


if __name__ == "__main__":
    input_path = "./day_04/test_input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
