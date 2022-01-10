#extentiions
import cv2
import numpy as np
from PIL import Image

for i in range(1314):
    
    #load images
    img=cv2.imread("0/a0 "+str(i+1).zfill(4)+".jpg") 
    imgpil=Image.open("0/a0 "+str(i+1).zfill(4)+".jpg")

    imgArray=np.asarray(img)

    #variable to start new lines
    count=0
    
    #open the output file
    f=open("out.txt","a")    
    
    f.write("$pic"+str(i+1).zfill(4)+":(")
    
    #process per pixel
    for x in range(imgpil.height):
        for y in range(imgpil.width):
            
            #get the color of the pixel and output 0(white) or 1(black)
            color=imgArray[x,y][2]
            if color<128:
                output=0
            else:
                output=1
                
            #to start new lines
            if count%imgpil.width==0:
                if count==0 :
                    f.write("("+str(output)+",")
                else:
                    f.write("),\n("+str(output)+",")
            elif count%imgpil.width==imgpil.width-1:
                f.write(str(output))
            else:
                f.write(str(output)+",")        
            count=count+1
    
    f.write("));\n\n")
    f.close()