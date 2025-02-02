from math import factorial
from typing import Generator, Tuple, List, TypeVar

from itertools import permutations

from puzzle_utils import get_conn_above, get_conn_below, get_conn_left, get_conn_right

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

def borders (width: int, height: int) :
  board_dims = (width, height)
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

    # if possible_edge_perms(all_edges, board_dims) == 1:
    #   continue
    # print_connections(all_edges, (width, height))
    # print("")
    # for inner_pairings in pair_off(inner_edges):
    #   for j, (first_inner_conn, second_inner_conn) in enumerate(inner_pairings):
    #     all_edges[first_inner_conn] = i + j
    #     all_edges[second_inner_conn] = i + j
    #   print_connections(all_edges, (width, height))
    #   print("")
    for i in inner_edges:
      all_edges[i] = None

def edges_to_pieces (all_edges: List[int], board_dims: Tuple[int, int], border_only=False):
  w, h = board_dims

  get_piece = lambda r, c:  (
        None if get_conn_above(r, c, board_dims) == -1 else all_edges[get_conn_above(r, c, board_dims)], 
        None if get_conn_right(r, c, board_dims) == -1 else all_edges[get_conn_right(r, c, board_dims)], 
        None if get_conn_below(r, c, board_dims) == -1 else all_edges[get_conn_below(r, c, board_dims)], 
        None if get_conn_left(r, c, board_dims) == -1 else all_edges[get_conn_left(r, c, board_dims)] ) 
  if not border_only:
    return [get_piece(r, c)
        for r in range(h )for c in range(w)
    ]
  return [get_piece(0, c)
        for c in range(board_dims[0])
  ] + [get_piece(r, c)
        for c in (0, h-1)
        for r in range(h)
  ] + [ get_piece(h-1, c)
        for c in range(board_dims[0])
    
  ]



print(edges_to_pieces ([
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
], (3, 3))
)