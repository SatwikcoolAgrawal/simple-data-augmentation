import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def findTick(inputimg,temp):
    img = cv.imread(inputimg, cv.IMREAD_GRAYSCALE )
    assert img is not None, "file could not be read, check with os.path.exists()"
    img2 = img.copy()
    template = cv.imread(temp, cv.IMREAD_GRAYSCALE)
    assert template is not None, "file could not be read, check with os.path.exists()"
   
    w, h = template.shape[1::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 
                'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

    top_left=np.array([0,0])
   
    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
       
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left += np.array(min_loc)
        else:
            top_left += np.array(max_loc)
 
        
    
    padding=25
    top_left=top_left//len(methods)

    bottom_right = [top_left[0] + w, top_left[1] + h+padding]
    top_left[1]-=padding
    cv.rectangle(img,list(top_left),bottom_right, 0, 0)
    plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()  
    return list(top_left),bottom_right