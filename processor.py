import os
import shutil
from random import randint
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Processor:
    def __init__(self, image_picture):
        self.image = None
        self.dir = None
        self.filename = None
        self.image_picture = image_picture
        self.temp_dir = f'.tmp{randint(100001, 999998)}/'
        self.save_dir = 'Modified Images/'

    def image_load(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
        self.image = self.image.convert('RGB')

    def image_show(self, path):
        self.image_picture.hide()
        pixmapimage = QPixmap(path)
        w, h = self.image_picture.width(), self.image_picture.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        self.image_picture.setPixmap(pixmapimage)
        self.image_picture.show()

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.loader()
        image_path = os.path.join(self.dir, self.temp_dir, self.filename)
        self.image_show(image_path)

    def left_90(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.loader()
        image_path = os.path.join(self.dir, self.temp_dir, self.filename)
        self.image_show(image_path)

    def right_90(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.loader()
        image_path = os.path.join(self.dir, self.temp_dir, self.filename)
        self.image_show(image_path)

    def enhance(self):
        self.image = ImageEnhance.Contrast(self.image)
        self.image = self.image.enhance(1.5)
        self.loader()
        image_path = os.path.join(self.dir, self.temp_dir, self.filename)
        self.image_show(image_path)

    def bandw(self):
        self.image = self.image.convert('L')
        self.loader()
        image_path = os.path.join(self.dir, self.temp_dir, self.filename)
        self.image_show(image_path)

    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.loader()
        image_path = os.path.join(self.dir, self.temp_dir, self.filename)
        self.image_show(image_path)

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def loader(self):
        path = os.path.join(self.dir, self.temp_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    
    def delete_temp(self):
        if self.dir:
            path = os.path.join(self.dir, self.temp_dir)
            if os.path.exists(path) or os.path.isdir(path):
                shutil.rmtree(path)