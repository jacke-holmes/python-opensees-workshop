class Node():

    # constructor 
    def __init__(self, node_id: int, node_coords: list[float]):
        self.node_id = node_id

        assert len(node_coords) == 3, "You must have 3 coordinates"
        self.x: float = node_coords[0]
        self.y: float = node_coords[1]
        self.z: float = node_coords[2]
    
    def __repr__(self) -> str:
        return f"Node ({self.x, self.y, self.z})"