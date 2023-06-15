# start file
from typing import Any

# python import
from model import Model


model: Model = Model("2DFrame")  # instantiate the class

# adding nodes to model
model.nodes[1] = [0., 0., 0.]
model.nodes[2] = [0., 0., 3.]
model.nodes[3] = [4., 0., 3.]
model.nodes[4] = [4., 0., 0.]

# nodes: dict[int, list[float]] = {
#     1: n1,
#     2: n2,
#     3: n3,
#     4: n4
# }

# adding bars to model
model.bars[1] = [1, 2]  # column1
model.bars[2] = [4, 3]  # columns2
model.bars[3] = [2, 3]  # beam 1


print('model: ', model)
