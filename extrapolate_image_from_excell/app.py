#Importing the modules
import openpyxl
from convert_png_in_jpg import convert_png_in_jpg
from extrapolate_image_from_cell import extrapolate_image_from_cell

#loading the Excel File and the sheet
pxl_doc = openpyxl.load_workbook('demo.xlsx')
sheet = pxl_doc['Foglio1']

png_path = "media/png/"
jpg_path = "media/jpg/"

for row in sheet.iter_rows():
    code = row[0].value
    print(code)
    cell_position = str('C' + str(row[2].row))
    try:
        extrapolate_image_from_cell(sheet, cell_position, png_path, code, '.png')
        convert_png_in_jpg(png_path, jpg_path, code)
    except ValueError:
        print(ValueError)
        pass
