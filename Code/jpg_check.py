import glob
import cv2
from skimage import io

images = []



for img in glob.glob('C:/Projects/Waifu_recongizer/Code/Images/train/*.jpg'):
    try:
        img = io.imread(img)
    except:
        print(img)
    #print('true')