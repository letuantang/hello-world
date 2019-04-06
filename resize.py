# NOTE: 
# 1. CHÚ Ý ĐẶT TÊN FOLDER KHÔNG CÓ GẠCH CHÂN (GẠCH DƯỚI)
# 2. Sau khi chạy code mà không có ảnh trong thư mục thì xem lại .jpg hay .JPG

from PIL import Image
from resizeimage import resizeimage
import os, os.path
import glob, os

folder = "/TEST/"
current_dir = os.getcwd()
path = ''.join([current_dir, folder])

outdir = "oneside"
goal_dir = os.path.join(path, outdir)
#print (goal_dir)  # prints C:/here/I/am/../../my_dir
#print (os.path.normpath(goal_dir)) # prints C:/here/my_dir
#print (os.path.realpath(goal_dir)) # prints C:/here/my_dir
print (os.path.abspath(goal_dir)) # prints C:/here/my_dir
if not os.path.isdir(os.path.abspath(goal_dir)):
    os.mkdir(goal_dir)


filenames = glob.glob(path + "/*.jpg") #read all files in the path mentioned
#filenames = glob.glob(path + "/*.JPG") #read all files in the path mentioned

for x in filenames:
    file, ext = os.path.splitext(x)  # split filename and extension
    im = Image.open(x)
    #cover = resizeimage.resize_cover(im, [504, 378])
    cover = resizeimage.resize_cover(im, [672, 504])
    #cover = resizeimage.resize_cover(im, [1344, 1008])
    # construct output filename, basename to remove input directory

    save_fname = os.path.join(goal_dir, os.path.basename(file)+'.jpg')
    cover.save(save_fname)
print("Finish")
