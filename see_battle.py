import random
from canvas import Canvas


class Ship(object):
    '''
    Represent class Ship.
    '''
    def __init__(self, bow, length=(1, 1)):
        '''
        Initialise ship with it's details. First coordinate - width.
        '''
        self.bow = bow
        self._length = length
        self.horizontal = length[1] == 1
        self.hit = 0
        self.coordinates = self.generate_coordinates()

    def generate_coordinates(self):
        """
        Return list with the generated coordinates.
        """
        result = []
        if self.horizontal:
            for i in range(self._length[0]):
                current = (self.bow[0], self.bow[1]+i)
                result.append(current)
        else:
            for i in range(self._length[1]):
                current = (chr(ord(self.bow[0])+i), self.bow[1])
                result.append(current)

        return result


class Field(object):
    '''
    Represent class Field.
    '''
    def __init__(self):
        '''
        Generate list with ships.
        '''
        self.ships = []
        self.matrix = self.generate_matrix()
        self.canvas = Canvas(12, 12)
        self.canvas.add_rectangle((0, 0), (10, 10), border='')

        for i in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
            position = random.randint(0, 1)
            if position == 1:  # horizontal
                ship = (i, 1)
            else:
                ship = (1, i)

            checking = True
            while checking:
                bow = self.generate_coordinate()
                if self.check_place(ship, bow):
                    checking = False
                    self.ships.append(Ship(bow=bow, length=ship))

    def generate_coordinate(self):
        """
        Returns random coordinate.
        """
        return random.choice(self.matrix)

    def generate_matrix(self):
        """
        Generete matrix.
        """
        matrix = []
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
            for j in range(1, 11):
                matrix.append((i, j))
        return matrix

    def check_place(self, ship, coordinate):
        """
        Check if all ships can be placed on the field.
        """
        possible_coordinates = []
        reserved_coordinates = []

        if ship[1] == 1:
            for i in range(ship[0]):
                current = (coordinate[0], coordinate[1]+i)
                if current not in self.matrix:
                    return False
                possible_coordinates.append(current)
        else:
            for i in range(ship[1]):
                current = (chr(ord(coordinate[0])+i), coordinate[1])
                if current not in self.matrix:
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
            if i in self.matrix:
                self.matrix.remove(i)

        return True

    def shoot_at(self, coordinate):
        '''
        Shows if the rival hits the special cell on the field.
        '''
        for ship in self.ships:
            if coordinate in ship.coordinates:
                # draw Rectangle
                self.canvas.add_rectangle(((ord(coordinate[0])-65), coordinate[1]), (1, 1), border='X')
                return True
        return False


class Player(object):
    '''
    Represent class Player.
    '''
    def __init__(self, name, field):
        '''
        Initialise the player.
        '''
        self._name = name
        self._field = field
        self.hit = 0

    def read_position(self):
        '''
        Gets the coordinates of player's hit and converted them in the
        nessesary type.
        '''
        a = input('{} enter coordinates of hit: '.format(self._name))

        return (a[0], int(a[1]))


class Game(object):
    '''
    Represent class Game.
    '''
    def __init__(self):
        '''
        Informaition about game.
        '''
        self.players = [Player(name='Player 1', field=Field()), Player(name='Player 2', field=Field())]
        self._current_player = self.players[0]
        self._next_player = self.players[1]

    def start(self):
        """
        Function starts game and finishes it if someone wins.
        """
        print('Game is starting')
        flag = True
        while flag:
            turn = True
            while turn:
                shoot = self._current_player.read_position()
                if self._next_player._field.shoot_at(shoot):
                    self._current_player.hit += 1
                    if self._current_player.hit == 20:
                        print('{} WIN!'.format(self._current_player._name))
                        turn = flag = False
                    print('good shoot')
                    print(self._next_player._field.canvas)
                else:
                    turn = False
                    temp = self._current_player
                    self._current_player = self._next_player
                    self._next_player = temp
