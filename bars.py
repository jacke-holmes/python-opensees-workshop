from nodes import Node
from base_classes.thing import Thing

class Bar(Thing):
    
    # constructor 
    def __init__(self, bar_id: int, node_i: Node, node_j: Node):
        super().__init__(bar_id)

        assert isinstance(node_i, Node), "you must have entered a node object in node_i"
        assert isinstance(node_j, Node), "you must have entered a node object in node_j"
        assert node_i != node_j, "both nodes are the same node"

        self.node_end_i: Node = node_i
        self.node_end_j: Node = node_j
    
    def __repr__(self) -> str:
        return f"Bar ({self.node_end_i.thing_id, self.node_end_j.thing_id})"

    def get_node_ids_as_list(self):
        node_id_list: list[int] = list()

        node_id_list.append(self.node_end_i.thing_id)
        node_id_list.append(self.node_end_j.thing_id)

        return node_id_list