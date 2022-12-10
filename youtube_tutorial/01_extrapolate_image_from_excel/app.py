import openpyxl
from openpyxl_image_loader import SheetImageLoader

pxl_doc = openpyxl.load_workbook('cities.xlsx')
sheet = pxl_doc['Foglio1']
image_loader = SheetImageLoader(sheet)

image_folder = "images/"

for row in sheet.iter_rows():
    print(row[0].value)
    name = row[0].value
    cell_position = str("B" + str(row[1].row))
    try:
        image = image_loader.get(cell_position)
        image.save(image_folder + name + ".png")
    except:
        pass