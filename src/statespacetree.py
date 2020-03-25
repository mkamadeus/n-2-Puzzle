# statespacetree.py
# Contains the class StateSpaceTree to represent the state space tree in BnB

class StateSpaceTree:
    def __init__(self, root, parent = None, depth=0, move=""):
        self.root = root
        self.parent = parent
        self.move = move
        self.depth = depth
