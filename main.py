# main file of the program

# python import
from typing import Any
from model import Model

# Code starts here
model: Model = Model('2D_frame')

# adding nodes to model
model.nodes[1] = [0.,0.,0.]
model.nodes[2] = [0.,0.,3.]
model.nodes[3] = [4.,0.,3.]
model.nodes[4] = [4.,0.,0.]

# adding bars to model
model.bars[1] = [1 , 2]  # column 1
model.bars[2] = [4 , 3]  # column 2
model.bars[3] = [2 , 3]  # beam 1

print('model: ', model)