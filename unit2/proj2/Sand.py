class Sand:
    """
    Sand object - representing a single particle of sand in a Grid object
    stores Grid object and position in Grid
    """

    def __init__(self, grid, x=0, y=0):
        """
        creates Sand object with grid and position
        """
        self.grid = grid
        self.x = x
        self.y = y
        self.grid.set(x, y, self)

    def __str__(self):
        """
        prints human-readable string
        """
        return f"Sand({self.x},{self.y})"

    def gravity(self):
        """
        calls is_move_ok to validate proposed move
        returns valid position to move to, as (x, y) tuple
        """
        # start with straight down case
        if self.is_move_ok(self.x, self.y + 1):
            return self.x, self.y + 1
        # move to diagonal cases - first down-left
        elif self.is_move_ok(self.x - 1, self.y + 1):
            return self.x - 1, self.y + 1
        # then down-right
        elif self.is_move_ok(self.x + 1, self.y + 1):
            return self.x + 1, self.y + 1
        # if no valid moves, return current position
        else:
            return self.x, self.y

    def is_move_ok(self, x_to, y_to):
        """
        checks if move is valid
        """
        try:
            # start with straight down case
            if self.x == x_to:
                if self.grid.get(x_to, y_to) is None:
                    return True
                else:
                    return False
            # move to diagonal cases
            else:
                if self.grid.get(x_to, y_to) is None and self.grid.get(x_to, y_to - 1) is None:
                    return True
                else:
                    return False
        except IndexError:
            return False

    def move(self, physics):
        """
        call physics to get destination
        update self position in grid
        update self x, y, and grid values
        """
        x_to, y_to = physics()
        if x_to is None or y_to is None:
            return
        self.grid.set(self.x, self.y, None)
        self.grid.set(x_to, y_to, self)
        self.x = x_to
        self.y = y_to
