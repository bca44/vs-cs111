from Grid import Grid
from copy import deepcopy
import random


def print_grid(grid):
    """
    prints Grid object with all row elements
    on single line, separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()


def modify_grid(grid, func, prob):
    """
    Write a function which can take in a grid, a function
    and a probability as parameters and updates the grid using
    the function passed in
    """
    for y in range(grid.height):
        for x in range(grid.width):
            if random.random() <= prob:
                func(grid, x, y)
    return grid


def random_rocks(grid, chance_of_rock):
    """
    Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.
    """
    new_grid = deepcopy(grid)
    return modify_grid(new_grid, lambda grid, x, y: grid.set(x, y, "r"), chance_of_rock)


def random_bubbles(grid, chance_of_bubbles):
    """
    Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position
    """
    new_grid = deepcopy(grid)
    return modify_grid(new_grid, lambda grid, x, y: grid.set(x, y, "b"), chance_of_bubbles)


def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    grid1 = deepcopy(grid)
    if grid1.get(x, y) == "b" and grid1.get(x, y - 1) != "b":
        try:
            grid1.in_bounds(x, y - 1)
            grid1.set(x, y, None)
            grid1.set(x, y - 1, "b")
        except IndexError:
            print(f"Index Error at ({x}, {y - 1}).")
    return grid1


def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    def bubble_func(grid, x, y):
        try:
            if grid.get(x, y) == "b" and grid.get(x, y - 1) != "b":
                grid.in_bounds(x, y - 1)
                grid.set(x, y - 1, "b")
                grid.set(x, y, None)
        except IndexError:
            print(f"Index Error at ({x}, {y - 1}).")
    return modify_grid(grid, bubble_func, 1)


def animate_grid(grid, delay):
    """Given a Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1


if __name__ == "__main__":
    pass
