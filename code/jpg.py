import os
import glob
import shutil
from PIL import Image

def get_files(pattern):
    return glob.glob(pattern)

def process(pattern, quality=50):
    files = get_files(pattern)
    for file in files:
        # convert png to jpg with specified quality
        jpg_file = file.replace(".png", ".jpg")

        # get the absolute upper .. directory
        # if the jpg_file already exists in the upper .. directory, report and abort
        if os.path.exists(os.path.join("..", jpg_file)):
            print(f"Error: {jpg_file} already exists in ..")
            return
        with Image.open(file) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(jpg_file, 'JPEG', quality=quality)
    return files

process("*.png", quality=54)