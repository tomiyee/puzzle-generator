from tqdm import tqdm
from puzzle_generator import num_puzzles, puzzles

WIDTH = 2
HEIGHT = 4

for puzzle in tqdm(puzzles(WIDTH, HEIGHT), total=num_puzzles(WIDTH, HEIGHT)):
  pass