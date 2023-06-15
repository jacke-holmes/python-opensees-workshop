
#python import
from model import Model

#creating empty model
model: Model = Model("2D Frame") #instantiate the class 

#populating node geometry into the model 
model.nodes[1] = [0, 0, 0]     
model.nodes[2] = [0, 0, 3]
model.nodes[3] = [4, 0, 3]
model.nodes[4] = [4, 0, 0]

#nodes: dict[int, list[float]] = {
 #   1: n1,
  #  2: n2, 
   # 3: n3,
    #4: n4
#    }

#adding bars to model
model.bars[1] = [1, 2] #columns 1
model.bars[1] = [4, 3] #columns 2
model.bars[1] = [2,3]  #beam 1

print('model: ', model)
