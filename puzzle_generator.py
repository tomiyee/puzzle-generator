from math import floor
from typing import Generator, Tuple, List

from itertools import permutations

PuzzlePiece = Tuple[int, int, int, int]
"""
A puzzle piece
Numbers given in order of North, East, South, West orientation
"""

def puzzle_generator(width: int, height: int, solutions = 2) -> Generator[List[PuzzlePiece], None, None]:
  """Generates """
  num_connections = (width-1)*height + (height-1)*width
  num_unique_connections = num_connections//solutions
  all_connections = [(n % num_unique_connections) + 1 for n in range(num_connections)]
  for perm in permutations(all_connections):
    puzzle = []
    for r in range(height):
      for c in range(width):
        connection_n = 0 if r is 0 else perm[(width-1) * r + width * (r-1) + c % width]
        connection_s = 0 if r is height - 1 else perm[(width-1) * (r+1) + width * r + c % width]
        connection_e = 0 if c is width - 1 else perm[(width-1) * (r) + width * r + c % width]
    yield perm
for p in puzzle_generator(5, 5):
  print(p)