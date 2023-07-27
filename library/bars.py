from library.base_classes.thing import Thing
from library.nodes import Node


class Bar(Thing):

    # constructor
    def __init__(self, bar_id: int, node_i: Node, node_j: Node):
        super().__init__(bar_id)

        assert isinstance(node_i, Node), "you must have node i entered a node object"
        assert isinstance(node_j, Node), "you must have node j entered a node object"
        assert node_i != node_j, "both nodes are the same node"

        self.node_end_i: Node = node_i
        self.node_end_j: Node = node_j

    def __repr__(self) -> str:
        return f"Bar {(self.node_end_i.thing_id, self.node_end_j.thing_id)}"

    def get_node_ids_as_list(self) -> list[int]:
        node_id_list: list[int] = list()

        node_id_list.append(self.node_end_i.thing_id)
        node_id_list.append(self.node_end_j.thing_id)

        return node_id_list