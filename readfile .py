import xlrd
#打开excel文件
excel=xlrd.open_workbook("C:\\Users\\lenovo\\Desktop\\test.xls")
#获取第一个sheet
sheet1=excel.sheets()[0]
#打印第I行数据
nrows=sheet1.nrows
ncols=sheet1.ncols
for i in range (1,nrows):
    print(sheet1.row_values(i))
#打印第J列数据
for j in range (1,ncols):
    print(sheet1.col_values(j))
