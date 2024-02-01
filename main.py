# Import the necessary modules
import os
from findTick import findTick
from image_cropping import cropImage 
from textRecognition import findText
import cv2 as cv


source_folder = "C:\projects\data augumentation\dataimg"

destination_folder = "dataset"


def partypredictor(input):
    top_left,bottom_right=findTick(input,'template.png')
    cropped_image=cropImage(input,top_left[1],bottom_right[1])
    texts=findText(cropped_image)
    return texts[0]


image_file=input("enter file name :")
print(partypredictor(image_file))


