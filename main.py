# Start file

from typing import Any
from model import Model

model: Model = Model("2DFrame")  # Instantiate the class 

# Adding notes to model, with coordinates x, y, z
model.nodes[1] = [0., 0., 0.]
model.nodes[2] = [0., 0., 3.]
model.nodes[3] = [4., 0., 3.]
model.nodes[4] = [4., 0., 0.]

# Adding bars to model
model.bars[1] = [1, 2]  # Column 1
model.bars[2] = [4, 3]  # Column 2
model.bars[3] = [2, 3]  # Beam

print('model: ', model)