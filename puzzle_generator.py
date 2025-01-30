from math import factorial
from typing import Generator, Tuple, List

from itertools import permutations

PuzzlePiece = Tuple[int, int, int, int]
"""
A puzzle piece
Numbers given in order of North, East, South, West orientation
"""

def puzzles(width: int, height: int, solutions = 2) -> Generator[List[PuzzlePiece], None, None]:
  """Generates """
  num_connections = (width-1)*height + (height-1)*width
  num_unique_connections = num_connections//solutions
  all_connections = [(n % num_unique_connections) + 1 for n in range(num_connections)]
  for perm in permutations(all_connections):
    puzzle = []
    for r in range(height):
      for c in range(width):
        n_index = (width-1) * r + width * (r-1) + (c % width)
        w_index = (width-1) * r + width * r + (c % width) - 1
        n = 0 if r == 0 else perm[n_index]
        w = 0 if c == 0 else perm[w_index]
        e = 0 if c == width - 1 else perm[w_index + 1]
        s = 0 if r == height - 1 else perm[n_index  + (width-1) + width]
        puzzle.append((n, e, s, w))
    yield puzzle
    
def num_puzzles(width: int, height: int) -> int:
  return factorial( (width-1)*height + (height-1)*width)
