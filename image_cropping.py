import cv2
import numpy as np
import matplotlib.pyplot as plt

# # Read the image
# img = cv2.imread('votingslip.jpg')

#     # Crop the image
# cropped_img = img[366:462, :]

#     # Save the cropped image
# cv2.imwrite("cropped_image.jpg", cropped_img)


def cropImage(input,y1,y2):
    img = cv2.imread(input)

    # Crop the image
    cropped_img = img[y1:y2, :]
    plt.imshow(cropped_img,cmap = 'gray')
    plt.title('Cropped Image'), plt.xticks([]), plt.yticks([])
    plt.show()  

    return cropped_img