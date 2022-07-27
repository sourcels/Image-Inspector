import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QMessageBox, QInputDialog, QHBoxLayout, QVBoxLayout, QFileDialog

from processor import Processor            

image_app = QApplication([])
image_main = QWidget()
image_main.resize(700, 500) 

image_folder = QPushButton('Choose Folder')
image_left90 = QPushButton('Left')
image_right90 = QPushButton('Right')
image_mirror = QPushButton('Mirror')
image_enhance = QPushButton('Enhance')
image_bandw = QPushButton('B/W')
image_blur = QPushButton('Blur')
image_save = QPushButton('Save image')

image_picture = QLabel('Image may be here...')

image_folder_list = QListWidget()

image_message = QMessageBox()

image_input = QInputDialog()

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
h3.addWidget(image_save)

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

def buttons_hide(param):
    image_blur.setEnabled(param)
    image_left90.setEnabled(param)
    image_right90.setEnabled(param)
    image_mirror.setEnabled(param)
    image_enhance.setEnabled(param)
    image_bandw.setEnabled(param)
    image_blur.setEnabled(param)
    image_save.setEnabled(param)

def showFilenamesList():
    image_extensions = ['.jpg', '.jpeg', '.png', '.tif', '.tiff', '.bmp', '.dib', '.webp']
    chooseWorkdir()
    try:
        filenames = filter(os.listdir(image_workdir), image_extensions)
        image_folder_list.clear()
        for filename in filenames:
            image_folder_list.addItem(filename)
    except:
        pass


def showImage():
    filename = image_folder_list.currentItem().text()
    wandImage.image_load(image_workdir, filename)
    image_path = os.path.join(wandImage.dir, wandImage.filename)
    wandImage.image_show(image_path)
    buttons_hide(True)

wandImage = Processor(image_picture, image_message, image_input)

image_folder_list.currentRowChanged.connect(showImage)

image_folder.clicked.connect(showFilenamesList)
image_mirror.clicked.connect(wandImage.mirror)
image_left90.clicked.connect(wandImage.left_90)
image_right90.clicked.connect(wandImage.right_90)
image_enhance.clicked.connect(wandImage.enhance)
image_bandw.clicked.connect(wandImage.bandw)
image_blur.clicked.connect(wandImage.blur)
image_save.clicked.connect(wandImage.saveImage)

image_app.aboutToQuit.connect(wandImage.delete_temp)

buttons_hide(False)

image_main.show()
image_app.exec_()