# pkgs
import numpy as np
import cv2

# load img
img = cv2.imread('cat.jpg')
img = cv2.resize(img, (800, 600))


# Convolution Operation On imgs
# covolution is complex mathamatical operation  which is apply kernel matrix on exisitnig imgs


def covert_img_to_greyscale():
    # covert to greyscale
    img_greyscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('cat-greyscale',img_greyscale)

def resize_img():
    # resize img to 100x100
    img_resized = cv2.resize(img,(100,100))
    cv2.imshow('cat-resied',img_resized)

# enhcning edges
def sharpen_img():
    # kernel matrix used to shapen matrix
    # commonlly used 3*3 matrix which gives more detailed feature / edges
    # we can go for 5x5 or more but lower matrix more detailed freatures it gives 
    # thus kernels values are already defined to perform convolution operations
    # we can chnage intensity of sharpen by middle most value here is 5
    kernel = np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ])

    ## sharpen img using kernel matrix (matrix used to perform required operation)
    img_shapren = cv2.filter2D(img,-1,kernel) #(img,depth,kernel)
    cv2.imshow('shapren-img',img_shapren)


# embos img
def emboss_img():
    # imboss kernel
    kernel = np.array([
        [-2,-1,0],
        [-1,1,1],
        [0,1,2]
    ])

    img_greyscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_emboss = cv2.filter2D(img_greyscale,-1,kernel)
    cv2.imshow('embossed-img',img_emboss)


def blur_img():
    # blur kernel
    # kernel = np.array([
    #     [0.0625,0.125,0.0625],
    #     [0.125,0.25,0.125],
    #     [0.0625,0.125,0.0625]
    # ])

    kernel = np.array([
            [1,1,1],
            [1,1,1],
            [1,1,1]
        ])/20
    img_blur = cv2.filter2D(img,-1,kernel)
    cv2.imshow('blured-img',img_blur)

# edge 
def detect_edge():
    # 
    kernel = np.array([
        [-1,-1,-1],
        [-1,8,-1],
        [-1,-1,-1]
    ])
    img_egde = cv2.filter2D(img,-1,kernel)
    cv2.imshow('edges-of-img',img_egde)


# show original img
cv2.imshow('original-img',img)
# show img to greyscale
# covert_img_to_greyscale()

# resized img
# resize_img()

# sharpen img
# sharpen_img()

# emboss img
# emboss_img()

# bulr img
# blur_img()

# edges
detect_edge()

# wait for user to enter key
cv2.waitKey(0)

# destory all the windows
cv2.destroyAllWindows()

# for kernels prefere : https://setosa.io/ev/image-kernels/