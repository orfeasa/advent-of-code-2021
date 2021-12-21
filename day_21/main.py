from collections import Counter, defaultdict
from dataclasses import dataclass


def part_one(filename: str) -> int:
    with open(filename) as f:
        player1_pos, player2_pos = list(
            map(lambda line: int(line.strip()[-1]), f.readlines())
        )
    player1_score, player2_score = 0, 0
    rolls = 0
    player1_turn = True
    while player1_score < 1000 and player2_score < 1000:
        rolls += 1
        move = (rolls * 3 + 1) * 3 + 3
        if player1_turn:
            player1_pos = (player1_pos + move) % 10 + 1
            player1_score += player1_pos
        else:
            player2_pos = (player2_pos + move) % 10 + 1
            player2_score += player2_pos
        player1_turn = not player1_turn

    return min(player1_score, player2_score) * (rolls * 3)


@dataclass
class State:
    score_pl1: int = 0
    score_pl2: int = 0
    pos_pl1: int = 1
    pos_pl2: int = 1

    def __hash__(self):
        return hash((self.score_pl1, self.score_pl2, self.pos_pl1, self.score_pl2))

    def __eq__(self, other):
        return (self.score_pl1, self.score_pl2, self.pos_pl1, self.score_pl2) == (
            other.score_pl1,
            other.score_pl2,
            other.pos_pl1,
            other.score_pl2,
        )

    def __ne__(self, other):
        return not (self == other)


def part_two(filename: str) -> int:
    with open(filename) as f:
        player1_pos, player2_pos = list(
            map(lambda line: int(line.strip()[-1]), f.readlines())
        )

    states = defaultdict(int)
    states[State(0, 0, player1_pos, player2_pos)] = 1

    count_wins_1, count_wins_2 = 0, 0
    player1_turn = True
    while states:
        states = update_positions(states, player1_turn)
        for state in list(states.keys()):
            if state.score_pl1 >= 21:
                count_wins_1 += states[state]
                del states[state]
            if state.score_pl2 >= 21:
                count_wins_2 += states[state]
                del states[state]
        player1_turn = not player1_turn
    return max(count_wins_1, count_wins_2)


def update_positions(states: dict["State", int], player1_turn: bool):
    rolls = Counter(
        [i + 1 + j + 1 + k + 1 for i in range(3) for j in range(3) for k in range(3)]
    )
    new_states = defaultdict(int)
    for state in states:
        for roll, universes in rolls.items():
            if player1_turn:
                new_pos = (state.pos_pl1 + roll - 1) % 10 + 1
                new_state = State(
                    state.score_pl1 + new_pos, state.score_pl2, new_pos, state.pos_pl2
                )
            else:
                new_pos = (state.pos_pl2 + roll - 1) % 10 + 1
                new_state = State(
                    state.score_pl1, state.score_pl2 + new_pos, state.pos_pl1, new_pos
                )
            new_states[new_state] += states[state] * universes
    return new_states


if __name__ == "__main__":
    input_path = "./day_21/test_input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
