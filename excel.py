import openpyxl

owb=openpyxl.Workbook()
filename='myfile/myels.xlsx'
sheet=owb.active
sheet.title='mytile'

plama=[
    ["類別","編號","品名","單價","單位"],
    ["蔬菜","01","高麗菜","40","粒"],
    ["水果","02","草莓","500","箱"],
    ["堅果","03","杏仁","150","罐"]

]

sheet.cell(row=4,column=2,value="try")
owb.save(filename)
print("done")