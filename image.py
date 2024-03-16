import os
import cv2
import numpy as np
import zipfile

# Bluring of images with custom values  
def blurfn(img):
    if input==1:
        blur=cv2.medianBlur(img,kernal)
    elif input==2:
        blur=cv2.GaussianBlur(img,(0,0),4)
    else:
        blur=cv2.bilateralFilter(img,5,80,50)
    # sharpeing of image by blending 
    output=cv2.addWeighted(img,2,blur,-0.8,20)
    return output

# Reading folder directory and applying function by iterating loop for each image
def processing(f_path):
    image_files=os.listdir(f_path)
    images=[]
    for i in image_files:
        img_path=os.path.join(f_path,i)
        img=cv2.imread(img_path)
        output=blurfn(img)
        images.append((i,output))
    return images    

# Making a Zipfile of the output 
def zip(images):

    with zipfile.ZipFile('output.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
        for i,img in images:
            z.writestr(i,cv2.imencode('.png',img)[1].tobytes())

# User inp
f_path=input("Enter path of the folder containing Images: ")
input=str(input("what type of blur you want?\noptions:\n 1) Median Blur\n 2)Gaussian Blur\n 3)Bilateral Blur"))
images=processing(f_path)
zip(images)
print("output images are saved in 'output.zip' ")





























