'''
open image .pngand save it as .png
in case png image is RGBA convert in RGB
'''
from PIL import Image

'''
png_path = "media/png/"
jpg_path = "media/jpg/"
image_name = "xxxx"
'''
def convert_png_in_jpg(png_path, jpg_path, image_name):
    image = Image.open(r'' + png_path + image_name + '.png')
    image_rgb = image.convert('RGB')
    image_rgb.save(r'' + jpg_path + image_name + '.jpg')