import collections


class food_tree:
    def __init__(self, tree:dict):
        self.tree = tree

    def add_node(self, val: str, fathers:list):
        # root: a list contains each father node
        # only add some nodes in the same level
        # vals must be list, containing one or more nodes
        root = self.tree
        for father in fathers:
            root = root[father]
        # for val in vals:
        root[val] = {}

    def delete_node(self, val: str, fathers:list):
        root = self.tree
        for father in fathers:
            root = root[father]
        # for val in vals:
        del root[val]