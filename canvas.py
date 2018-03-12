class Rectangle:
    def __init__(self, corner, size, border='*', inside=' '):
        """
        Initialize new rectangle.
        :param corner: corner coordinates.
        :param size: size of rectangle
        :param border: symbol that is used to display rectangle border.
        :param inside: symbol that is used to display rectangle border.
        """
        self._corner = corner
        self._size = size
        self.border = border
        self.inside = inside

    def view(self, coordinate):
        """
        Display view of rectangle by coordinate.
        :param coordinate: coordinate of cell.
        :return: view of rectangle by coordinate.
        """
        if coordinate[0] == self._corner[0] or coordinate[1] == self._corner[1] or \
           coordinate[0] == self._corner[0] + self._size[0] - 1 or coordinate[1] == self._corner[1] + self._size[1] - 1:
            return self.border
        else:
            return self.inside


class Canvas:
    def __init__(self, width, height):
        """
        Initialize new canvas.
        :param width: canvas width.
        :param height: canvas height.
        """
        self.width = width
        self.height = height
        self.cells = [[None] * width for i in range(height)]

    def add_rectangle(self, corner, size, border='*', inside=' '):
        """
        Add rectangle to canvas.
        :param corner: corner coordinates.
        :param size: size of rectangle
        :param border: symbol that is used to display rectangle border.
        :param inside: symbol that is used to display rectangle border.
        :return: recatngle that has been added.
        """
        r = Rectangle(corner, size, border=border, inside=inside)
        for i in range(size[0]):
            for j in range(size[1]):
                coordinate = (corner[0] + i, corner[1] + j)
                if 0 <= coordinate[0] < self.height and 0 <= coordinate[1] < self.width:
                    if self.cells[coordinate[0]][coordinate[1]] != None:
                        self.cells[coordinate[0]][coordinate[1]].append(r)
                    else:
                        self.cells[coordinate[0]][coordinate[1]] = [r]
        return r

    def __str__(self):
        """
        View of canvas.
        :return: view of canvas.
        """
        s = ''
        for i in range(self.height):
            for j in range(self.width):
                cell = self.cells[i][j]
                if cell != None:
                    s += cell[-1].view((i, j))
                else:
                    s += ' '
            s += '\n'
        return s
