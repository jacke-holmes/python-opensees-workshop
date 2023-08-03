import xlwings as xw

# connect to a workbook
path = "C:\\Workspace\\Holmes\\OpenSeesTools\\python-opensees-workshop\\input.xlsx"
wb = xw.Book(path)
print("Workbook name: ", wb.name)

# connect to a sheet
input_sheet = wb.sheets['input']
cell = input_sheet.range('D6')

x1 = input_sheet.range('E6').value
y1 = input_sheet.range('F6').value
z1 = input_sheet.range('G6').value

# node_table1 = input_sheet.range('C6:G9')
node_table = input_sheet.range('nodeTable')

for node_row in node_table.value:
    print("ID: ", node_row[0])
    print("X: ", node_row[2])

# then we do stuff - ranges, tables, charts
# push and pull to and from the workbook to our codebase

print(0)
