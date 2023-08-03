import xlwings as xw

# connect to workbook
wb = xw.Book("C:\\Workspace\\Holmes\\OpenSeesTools\\python-opensees-workshop\\examples\\input.xlsx")
print(wb.name)

ws = wb.sheets["Sheet1"]
print(ws.name)

nodes = ws.range('nodeTable')

wb.close()
