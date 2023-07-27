# start file
from typing import Any

# python import
from library.model import Model
from library.nodes import Node
from library.bars import Bar


model: Model = Model("2DFrame")  # instantiate the class

# adding nodes to model
model.nodes[1] = Node(1, [0., 0., 0.])
model.nodes[2] = Node(2, [0., 0., 3.])
model.nodes[3] = Node(3, [4., 0., 3.])
model.nodes[4] = Node(4, [4., 0., 0.])

# adding bars to model
model.bars[1] = Bar(1, model.nodes[1], model.nodes[2]) # [1, 2] column 1
model.bars[2] = Bar(2, model.nodes[4], model.nodes[3]) # [4, 3] column 2
model.bars[3] = Bar(3, model.nodes[2], model.nodes[3]) # [2, 3] beam 1

my_node_coords = model.nodes[4].get_node_coords_as_list()
print("my_nodes coords: ", my_node_coords)

print('model: ', model)