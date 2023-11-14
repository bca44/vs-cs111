class Grid:
    """
    2D grid with (x, y) indexed internal storage
    and .width .height size properties
    """

    def __init__(self, width, height):
        """
        creates Grid object with width, height, and array
        all locations hold None
        """
        self.width = width
        self.height = height
        self.array = [[None for i in range(width)] for j in range(height)]

    def __str__(self):
        """
        prints human-readable string
        Grid(<height>, <width>, first = <first element>)
        """
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __repr__(self):
        """
        The __repr__ function is supposed to return a string
        that if we pasted it into a Python script or called Python's eval() function, would recreate the object.
        For now, returns same as __str__ method.
        """
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def in_bounds(self, x, y):
        """
        validates (x, y) position as in bounds
        """
        if not (0 <= x <= self.width and 0 <= y <= self.height):
            raise IndexError

    def get(self, x, y):
        """
        gets the value stored value at (x, y).
        (x, y) should be in bounds.
        """
        try:
            self.in_bounds(x, y)
            return self.array[y][x]
        except IndexError:
            print(f"Index Error at ({x}, {y}).")

    def set(self, x, y, val):
        """
        sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        """
        try:
            self.in_bounds(x, y)
            self.array[y][x] = val
        except IndexError:
            print(f"Index Error at ({x}, {y}).")
