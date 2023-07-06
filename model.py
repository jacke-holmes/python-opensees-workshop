from nodes import Node
from bars import Bar


class Model():

    # constructor
    def __init__(self, model_name: str):
        self.name = model_name

        self.nodes: dict[int, Node] = dict()
        self.bars: dict[int, Bar] = dict()

    def print_name(self):
        print(self.name)

    @property
    def p_node_count(self):
        return len(self.nodes)

    @p_node_count.setter
    def p_node_count(self, number: int):
        raise Exception("you should not modify the node count directly")

    @property
    def p_bar_count(self):
        return len(self.bars)
