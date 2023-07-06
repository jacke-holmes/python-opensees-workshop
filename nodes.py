from base_classes.thing import Thing


class Node(Thing):

    # constructor
    def __init__(self, node_id: int, node_coords: list[float]):
        super().__init__(node_id)

        assert len(node_coords) == 3, "you must have 3 node coordinates"

        self.x: float = node_coords[0]
        self.y: float = node_coords[1]
        self.z: float = node_coords[2]

    def __repr__(self) -> str:
        return f"Node {(self.x, self.y, self.z)}"

    def get_node_coords_as_list(self) -> list[float]:

        # coord_list: list[float] = list()
        # coord_list.append(self.x)
        # coord_list.append(self.y)
        # coord_list.append(self.z)

        return [self.x, self.y, self.z]



