from math import factorial
from typing import Generator, Tuple, List, TypeVar

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


# for every possible generated edge
#   for every permutation of the other three corners
#     if edges cannot fit new orientation of corners
#       skip
#     first_border_pieces_arrangement
#     second_border_pieces_arrangement
#     for every possible inner edge of first_border_pieces_arrangement
#       for every possible filling for first_border_pieces_arrangement
#         jig_solver(second_border_pieces_arrangement, filler_pieces)

# jig solver (board_state, pieces_remaining):
#   if board_state has no empty spaces
#     return [board_state]
#   solutions = []
#   for piece in pieces remaining
#     for rotation of piece
#       if it fits in the empty spot
#         solutions += jig_solver(board_state with fill, pieces without piece)
#   return solutions

T = TypeVar("A")

def gen_help (l: List[T]) -> Generator[List[T], None, None]:
  # Enumerate using https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

  
  pass

# border generator
# Choose (w-1) + (h-1) unique connections and choose them again from the bank
# Try every possible perm using lexicgraphic permutation



def lexicographic_generator(elems: List[T]) -> Generator[List[T],None, None]:
  result = sorted(elems)
  yield result 
  k_found = True
  while k_found:
    k_found = False
    for k in range(len(elems) - 2, -1, -1):
      if result[k] < result[k+1]:
        k_found = True
        for l in range(len(elems) - 1, k - 1, -1):
          if result[k] < result[l]:
            result[k], result[l] = result[l], result[k]
            result[k+1:] = result[k+1:][::-1]
            yield result
        break

    
def pair_off(l, avail=None):
  if len(l) % 2 != 0:
    return
  if avail == None:
    avail = set(range(len(l)))

  for first_index in avail:
    break

  first = l[first_index]
  avail.remove(first_index)
  available_indices = list(avail)
  for second_index in available_indices:
    second = l[second_index]
    t = (first, second)
    avail.remove(second_index)
    if len(avail) == 0:
      yield[t]
    else:
      for rest in pair_off(l, avail):
        yield [t] + rest
    avail.add(second_index)
  avail.add(first_index)

def get_conn_above (row: int, col: int, board_dims: Tuple[int, int]):
  w, h  = board_dims
  if row == 0: return -1
  return col + (2*w-1) * (row-1) + w - 1

def get_conn_below (row: int, col: int, board_dims: Tuple[int, int]):
  w, h  = board_dims
  if row == h-1: return -1
  return get_conn_above(row + 1, col, board_dims)

def get_conn_left (row: int, col: int, board_dims: Tuple[int, int]):
  w, h  = board_dims
  if col == 0: return -1
  return col + (2*w-1) * row - 1

def get_conn_right (row: int, col: int, board_dims: Tuple[int, int]):
  w, h  = board_dims
  if col == w-1: return -1
  return get_conn_left(row, col+ 1, board_dims) 

def borders (width: int, height: int) :
  num_connections = (width-1)*height + (height-1)*width

  top_row = [i for i in range(width-1)]
  bot_row = [i + (2 * width - 1)*(height-1) for i in range(width - 1)]
  left_col = [width - 1 + i * (2 * width - 1) for i in range(height - 1)]
  right_col = [2*(width - 1) + i * (2 * width - 1) for i in range(height - 1)]

  border_edges = top_row + left_col + right_col + bot_row
  inner_edges = [i for i in range(num_connections) if i not in border_edges]

  all_edges = [None for i in range(num_connections)]
  for border_pairings in pair_off(border_edges):
    for i, (first_conn, second_conn) in enumerate(border_pairings):
      all_edges[first_conn] = i
      all_edges[second_conn] = i
    print_connections(all_edges, (width, height))
    print("")




def print_connections (edges: List[int], board_dims: Tuple[int, int]):
  sq = " [ ] "
  width, height = board_dims
  format_edge = lambda n: "---" if n == None else f"{n:03d}"
  print(sq + sq.join([format_edge(edges[get_conn_right(0, c, board_dims)]) for c in range (width - 1)]) + sq)
  for r in range(1, height):
    print("   ".join([" " + format_edge( edges[get_conn_above(r, c,board_dims)]) + " " for c in range(width)]))
    print(sq + sq.join([format_edge(edges[get_conn_right(r, c, board_dims)]) for c in range (width - 1)]) + sq)

borders(3,3)