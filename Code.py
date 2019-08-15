import xlrd
import pymysql
pymysql.install_as_MySQLdb()

book = xlrd.open_workbook("Dataset.xlsx")
sheet = book.sheet_by_index(0)

database = pymysql.connect (host="localhost", user = "root", passwd = "paragk10", db = "mysqlPython")
cursor = database.cursor()

query0 = """DELETE FROM DataTable"""
cursor.execute(query0)

query = """INSERT INTO DataTable (instant, season, yr, mnth, holiday, weekday, workingday, weathersit, casual, registered, cnt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
           
for r in range(1, 732):
		a1	= sheet.cell(r,0).value
		a2	= sheet.cell(r,1).value
		a3		= sheet.cell(r,2).value
		a4		= sheet.cell(r,3).value
		a5		= sheet.cell(r,4).value
		a6 	= sheet.cell(r,5).value
		a7		= sheet.cell(r,6).value
		a8		= sheet.cell(r,7).value
		a9		= sheet.cell(r,8).value
		a10	= sheet.cell(r,9).value
		a11	= sheet.cell(r,10).value
		values = (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11)
		cursor.execute(query, values)

cursor.close()
database.commit()
database.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)

