from Grid import Grid

grid1 = Grid(4, 4)
print(grid1.array)
print(grid1)

for i in range(grid1.width):
    grid1.set(i, i, "!")

for y in range(grid1.height):
    for x in range(grid1.width):
        if grid1.get(x, y) is None:
            grid1.set(x, y, "*")

print(grid1.array)
print(grid1)
