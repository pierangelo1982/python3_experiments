'''
- this function extrapolate and image from a cell in excell .xlsx
'''
from openpyxl_image_loader import SheetImageLoader

'''
var explanations:

sheet = pxl_doc['Foglio1']
cell_position = "C4" colum C row 4 for example
path = "media/png/"
image_name = "xxxx"
extensions = ".png"

result in "media/png" you find the image
'''
def extrapolate_image_from_cell(sheet, cell_position, path, image_name, extension):
    image_loader = SheetImageLoader(sheet)
    image = image_loader.get(str(cell_position))
    image.save(path + image_name + extension)
