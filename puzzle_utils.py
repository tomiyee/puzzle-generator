
from typing import List, Tuple

Connections = List[int | None]
Width = int
Height = int
Dimensions = Tuple[Width, Height]

def get_conn_above (row: int, col: int, board_dims: Dimensions) -> int:
  w, h  = board_dims
  if row == 0: return -1
  return col + (2*w-1) * (row-1) + w - 1

def get_conn_below (row: int, col: int, board_dims: Dimensions) -> int:
  w, h  = board_dims
  if row == h-1: return -1
  return get_conn_above(row + 1, col, board_dims)

def get_conn_left (row: int, col: int, board_dims: Dimensions) -> int:
  w, h  = board_dims
  if col == 0: return -1
  return col + (2*w-1) * row - 1

def get_conn_right (row: int, col: int, board_dims: Dimensions) -> int:
  w, h  = board_dims
  if col == w-1: return -1
  return get_conn_left(row, col+ 1, board_dims) 


def print_connections (edges: Connections, board_dims: Dimensions):
  sq = " [ ] "
  width, height = board_dims
  format_edge = lambda n: "---" if n == None else f"{n:03d}"
  print(sq + sq.join([format_edge(edges[get_conn_right(0, c, board_dims)]) for c in range (width - 1)]) + sq)
  for r in range(1, height):
    print("   ".join([" " + format_edge( edges[get_conn_above(r, c,board_dims)]) + " " for c in range(width)]))
    print(sq + sq.join([format_edge(edges[get_conn_right(r, c, board_dims)]) for c in range (width - 1)]) + sq)
