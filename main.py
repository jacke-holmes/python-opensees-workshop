# start file
from typing import Any
import xlwings as xw

# python import
from library.model import Model
from library.nodes import Node
from library.bars import Bar


model: Model = Model("2DFrame")  # instantiate the class


# connect to model workbook
path = "C:\\Workspace\\Holmes\\OpenSeesTools\\python-opensees-workshop\\input.xlsx"
wb = xw.Book(path)

# connect to a sheet
input_sheet = wb.sheets['input']

# connect to node table
# node_count: int = 0
node_table = input_sheet.range('nodeTable').value
model.add_nodes_from_array(node_table)
# for row in node_table:
#     # node_count +=1
#     # adding nodes to model
#     node_id = row[0]
#     model.nodes[node_id] = Node(node_id, row[2:])

assert model.p_node_count == len(node_table), "all nodes have not been added to model"
input_sheet.range('nodeCount').value = model.p_node_count


# connect to BAR table
bar_table = input_sheet.range('barTable').value
for row in bar_table:
    print("Bar ID: ", row[0])


# # adding nodes to model
# model.nodes[1] = Node(1, [0., 0., 0.])
# model.nodes[2] = Node(2, [0., 0., 3.])
# model.nodes[3] = Node(3, [4., 0., 3.])
# model.nodes[4] = Node(4, [4., 0., 0.])



# adding bars to model
model.bars[1] = Bar(1, model.nodes[1], model.nodes[2]) # [1, 2] column 1
model.bars[2] = Bar(2, model.nodes[4], model.nodes[3]) # [4, 3] column 2
model.bars[3] = Bar(3, model.nodes[2], model.nodes[3]) # [2, 3] beam 1

my_node_coords = model.nodes[4].get_node_coords_as_list()
print("my_nodes coords: ", my_node_coords)


model.bars[1].node_end_i.y

print('model: ', model)
