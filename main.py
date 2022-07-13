import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QListWidget, QFileDialog

from processor import Processor            

image_app = QApplication([])
image_main = QWidget()
image_main.resize(700, 500) 

image_folder = QPushButton('Папка')
image_left90 = QPushButton('Лево')
image_right90 = QPushButton('Право')
image_mirror = QPushButton('Зеркально')
image_enhance = QPushButton('Резкость')
image_bandw = QPushButton('Ч/Б')
image_blur = QPushButton('Размытие')
image_picture = QLabel('Image may be here')
image_folder_list = QListWidget()

h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()

h1.addLayout(v1)
h1.addLayout(v2)
v2.addLayout(h2)
v2.addLayout(h3)

v1.addWidget(image_folder)
v1.addWidget(image_folder_list)
h2.addWidget(image_picture)
h3.addWidget(image_left90)
h3.addWidget(image_right90)
h3.addWidget(image_mirror)
h3.addWidget(image_enhance)
h3.addWidget(image_bandw)
h3.addWidget(image_blur)

image_main.setLayout(h1)

image_workdir = None
def filter(files, image_extensions):
    result = []
    for filename in files:
        for ext in image_extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
    
def chooseWorkdir():
    global image_workdir
    image_workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    image_extensions = ['.jpg','.jpeg','.png','.gif','.tif','.tiff','.bmp','.dib','.webp']
    chooseWorkdir()
    try:
        filenames = filter(os.listdir(image_workdir), image_extensions)
        image_folder_list.clear()
        for filename in filenames:
            image_folder_list.addItem(filename)
    except:
        pass
image_folder.clicked.connect(showFilenamesList)

def showImage():
    filename = image_folder_list.currentItem().text()
    wandImage.image_load(image_workdir, filename)
    image_path = os.path.join(wandImage.dir, wandImage.filename)
    wandImage.image_show(image_path)

wandImage = Processor(image_picture)
image_folder_list.currentRowChanged.connect(showImage)
image_mirror.clicked.connect(wandImage.mirror)
image_left90.clicked.connect(wandImage.left_90)
image_right90.clicked.connect(wandImage.right_90)
image_enhance.clicked.connect(wandImage.enhance)
image_bandw.clicked.connect(wandImage.bandw)
image_blur.clicked.connect(wandImage.blur)

image_main.show()
image_app.exec_()
