class Table:
    def __init__(self, state):
        self.state = state
        self.positions = [8][8]
    def getState(self):
        return self.state
    def setState(self, state):
        self.state = state
    def start(self):
        pass
#só dá pra setar a cor na inicialização da peça
class Pawn:
    def __init__(self, position, color, alive):
        self.position = position
        self.color = color
        self.alive = alive
    def getPosition(self):
        return self.position
    def getColor(self):
        return self.color
    def setPosition(self, position):
        self.position = position
    def isAlive(self, isAlive):
        return self.alive

class Bishop:
    def __init__(self, position, color, alive):
        self.position = position
        self.color = color
        self.alive = alive
    def getPosition(self):
        return self.position
    def getColor(self):
        return self.color
    def setPosition(self, position):
        self.position = position
    def isAlive(self, isAlive):
        return self.alive

class Queen:
    def __init__(self, position, color, alive):
        self.position = position
        self.color = color
        self.alive = alive
    def getPosition(self):
        return self.position
    def getColor(self):
        return self.color
    def setPosition(self, position):
        self.position = position
    def isAlive(self, isAlive):
        return self.alive

class King:
    def __init__(self, position, color, alive):
        self.position = position
        self.color = color
        self.alive = alive
    def getPosition(self):
        return self.position
    def getColor(self):
        return self.color
    def setPosition(self, position):
        self.position = position
    def isAlive(self, isAlive):
        return self.alive

class Knight:
    def __init__(self, position, color, alive):
        self.position = position
        self.color = color
        self.alive = alive
    def getPosition(self):
        return self.position
    def getColor(self):
        return self.color
    def setPosition(self, position):
        self.position = position
    def isAlive(self, isAlive):
        return self.alive

class Rook:
    def __init__(self, position, color, alive):
        self.position = position
        self.color = color
        self.alive = alive
    def getPosition(self):
        return self.position
    def getColor(self):
        return self.color
    def setPosition(self, position):
        self.position = position
    def isAlive(self, isAlive):
        return self.alive
class Piece:
    def __init__(self, position, color, alive, type):
        self.position = position
        self.color = color
        self.alive = alive
        self.type = type
    def getPosition(self):
        return self.position
    def getColor(self):
        return self.color
    def setPosition(self, position):
        self.position = position
    def isAlive(self, isAlive):
        return self.alive
