# start file
from typing import Any #import python file
from model import Model #from the file model, import the class model

frame: Model = Model('2dframe') # instantiation of the class, with this line the name is made but also the empty dict are made

frame.print_name()

# model: dict[str, Any] = {}

#making the coordinates directly into the model object
#adding nodes to the frame model (filled to the empty dictionary that is already made)
frame.nodes[1] = [0., 0., 0.]
frame.nodes[2] = [0., 0., 3.]
frame.nodes[3] = [4., 0., 3.]
frame.nodes[4] = [4., 0., 0.]

#dumb way of doing it
#n1: list[float] = [0., 0., 0.] # the . after the 0 gives the knowledge that it is a float
#n2: list[float] = [0., 0., 3.]
#n3: list[float] = [4., 0., 3.]
#n4: list[float] = [4., 0., 0.]

#nodes: dict[int, list[float]]={
#    1: n1,
#    2: n2,
#    3: n3,
#    4: n4
#}

#model['nodes']=nodes

#model['nodes'][4]

#print('model: ', model)

#adding bars to model (filled to the empty dictionary that is already made)
frame.bars[1] = [1, 2] #column1
frame.bars[2] = [4, 3] #column2
frame.bars[3] = [2, 3] #beam

frame.print_name()