import sys
import time

from board import Board
import heuristic as heuristics

from simpleai.search import (
    astar,
    breadth_first,
    depth_first,
    iterative_limited_depth_first
)
from simpleai.search.viewers import WebViewer

 

def main():
    start_board = Board.board_from_file(sys.argv[1])
    duplication_checks = sys.argv[2]
    method = sys.argv[3]
    heuristic = ''
    check_duplicates = 'graph' in duplication_checks

    if 'star' in method:
        heuristic = sys.argv[4]

        if heuristic == 'max_moves':
            start_board.heuristic = heuristics.max_moves
        elif heuristic == 'min_moves':
            start_board.heuristic = heuristics.min_moves
        elif heuristic == 'max_movable_pegs':
            start_board.heuristic = heuristics.max_movable_pegs
        elif heuristic == 'man':
            start_board.heuristic = heuristics.manhattan_distance
        else:
            print('You did not pick a viable heuristic. Exiting...')
            return

    start = time.time()
    if method == 'dfs':
        result = depth_first(start_board, check_duplicates)
    elif method == 'bfs':
        result = breadth_first(start_board, check_duplicates)

    elif method == 'astar':
        result = astar(start_board, check_duplicates)

    elif method == 'ildf':
        result = iterative_limited_depth_first(start_board, check_duplicates)

    else:
        print('You must choose a valid search method. Exiting...')
        return

    end = time.time()

    print("-" * 30)
    print('Search:', sys.argv[2], 'on', sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else '')
    print('Input File:', sys.argv[1])
    if result:
        path = result.path()
        for step in path:
            print(step[0], '-->', Board.board_from_state(step[1]))
        print('Duration: {0:.4f} seconds'.format(end - start))
        print('Nodes Visited:', len(path))

    else:
        print("No solution found!")


    print("-" * 30)


if __name__ == '__main__':
    main()
