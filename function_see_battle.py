def read_fields(path):
    """
    Reads field from file.
    """
    data = []
    with open(path) as file:
        for line in file.readlines():
            line = list(line)
            data.append(line)
    return data


def has_ship(data, coordinate):
    """
    Return True if ship is in coordinate.
    """
    if data[coordinate[0], coordinate[1]] == '*':
        return True
    else:
        return False


def is_valid(ship, coordinate, matrix):
    """
    Checks if all ships can be placed on the field.
    """
    possible_coordinates = []
    reserved_coordinates = []

    if ship[1] == 1:
        for i in range(ship[0]):
            current = (coordinate[0], coordinate[1]+i)
            if current not in matrix:
                return False
            possible_coordinates.append(current)
    else:
        for i in range(ship[1]):
            current = (chr(ord(coordinate[0])+i), coordinate[1])
            if current not in matrix:
                return False
            possible_coordinates.append(current)

    # add surround coordinates
    for i in possible_coordinates:
        up = (chr(ord(i[0])-1), i[1])
        right = (i[0], i[1]+1)
        down = (chr(ord(i[0])+1), i[1])
        left = (i[0], i[1]-1)
        reserved_coordinates.extend([i, up, right, left, down])

    # remove from matrix
    for i in reserved_coordinates:
        if i in matrix:
            matrix.remove(i)

    return True


def generate_field(a, b):
    """
    Generates field in special size.
    """
    matrix = []
    letters_list = []

    for i in range(65, 91):
        letters_list.append(chr(i))
    letter_for_matrix = letters_list[:a]

    for i in letter_for_matrix:
        for j in range(1, b+1):
            matrix.append((i, j))

    return matrix
   
