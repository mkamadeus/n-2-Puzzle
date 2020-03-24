class StateSpaceTree:
    def __init__(self, root, parent = None, depth=0, branches=[None, None, None, None]):
        self.root = root
        self.parent = parent
        self.depth = depth
        self.branches = branches

    # Create next state space
    def create_states(self):
        self.branches[0] = StateSpaceTree(self.root.move_up(), depth = self.depth+1, parent = self)
        self.branches[1] = StateSpaceTree(self.root.move_left(), depth = self.depth+1, parent = self)
        self.branches[2] = StateSpaceTree(self.root.move_right(), depth = self.depth+1, parent = self)
        self.branches[3] = StateSpaceTree(self.root.move_down(), depth = self.depth+1, parent = self)