import sys
import string
import pandas as pd

from cube import Cube


def reverse_moves(scramble: string) -> string:
    moves = scramble.split(' ')
    new_moves = []

    for move in moves:
        if move == "F":
            new_moves.append("F'")
        elif move == "B":
            new_moves.append("B'")
        elif move == "L":
            new_moves.append("L'")
        elif move == "R":
            new_moves.append("R'")
        elif move == "U":
            new_moves.append("U'")
        elif move == "D":
            new_moves.append("D'")
        elif move == "F'":
            new_moves.append("F")
        elif move == "B'":
            new_moves.append("B")
        elif move == "L'":
            new_moves.append("L")
        elif move == "R'":
            new_moves.append("R")
        elif move == "U'":
            new_moves.append("U")
        elif move == "D'":
            new_moves.append("D")
        else:
            new_moves.append(move)

    solution = ""
    for move in new_moves:
        solution = move + " " + solution
    solution = solution.strip()

    return solution


def get_label(size):
    label_array = [0]*19
    label_array[size-1] = 1
    return label_array


def format_data(infile_name: string, outfile_name: string):
    infile = open(infile_name, 'r')
    infile_lines = infile.readlines()

    X = []
    y = []

    for line in infile_lines:
        line_split = line.split('(')
        alg_decomposed = reverse_moves(line_split[0]).split(" ")
        num_turns = int(line_split[1].split('f')[0])

        alg = ""
        for i in range(num_turns):
            alg = (alg + " " + alg_decomposed[i]).strip()

            cube = Cube()
            cube.scramble(alg)
            X.append(cube.make_features())
            y.append(get_label(i + 1))

            del cube

    df = pd.DataFrame({"Scramble": X, "Distance": y})

    df.to_csv(outfile_name, sep='\t', index=False)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Three arguments are required")
        exit()

    format_data(sys.argv[1], sys.argv[2])
