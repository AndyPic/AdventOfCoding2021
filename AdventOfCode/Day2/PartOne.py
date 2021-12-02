# Get data into list
with open("Day2\Data.txt") as file:
    lines = file.readlines()


class Vector2:
    x = int(0)
    y = int(0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    def __str__(self) -> str:
        return "x: {}, y: {}".format(self.x, self.y)


def PositionDelta(line: tuple) -> Vector2:
    if line[0] == "up":
        return Vector2(0, -line[1])
    if line[0] == "down":
        return Vector2(0, line[1])
    if line[0] == "forward":
        return Vector2(line[1], 0)
    print("Something went wrong...")


startPos = Vector2(0, 0)
endPos = startPos

tupleLines = []
# Strip crap off, and format
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    line = lines[i].split()
    tupleLines.append((line[0], int(line[1])))
    endPos += PositionDelta(tupleLines[i])

print(endPos)
print("Answer = {}".format(endPos.x * endPos.y))
