# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:49:36 2017

@author: DIG
"""
import dicom
import cv2
import os
import numpy as np
from skimage import io
from skimage import img_as_ubyte
def process_image(fina,pathone, dir_Path,new_root):
    
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        subdir_split = root.split('/')
        print subdir_split[3]
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            if '-icontour-manual.txt' in fileobj:
                print fileobj
            else:
                continue
            txtname = fileobj.split('-')
            imagename=fina+txtname[-3]+'.dcm'
            originalimage=os.path.join(pathone,imagename)
            image = dicom.read_file(originalimage)
            image = image.pixel_array.astype(float)
            image /= np.max(image)
            image=image*255
            new_name=subdir_split[3]+'_'+txtname[-3]+'.png'
            new_nameM=subdir_split[3]+'_'+txtname[-3]+'M.png'
            new_nameL=subdir_split[3]+'_'+txtname[-3]+'L.png'
            originalimage=os.path.join(new_root,new_name)
            new_nameM=os.path.join(new_root,new_nameM)
            new_nameL=os.path.join(new_root,new_nameL)
            cv2.imwrite(originalimage,image)
            xx=image.shape[0]
            yy=image.shape[1]
            image2 = np.zeros((xx,yy,1), np.uint8) 
            #for line in open('F:\LV2009\label\SC-HF-I-01\contours-manual\IM-0001-0048-icontour-manual.txt'):
            pts = np.array([[0,0]], np.int) 
            i=0
            #for line in open('F:\IM-0001-0048-icontour-manual.txt'):
            for line in open(old_path):
                i+=1
                #print line
                line = line.strip('\n')
                nums = line.split(" ")
                nums = [float(x) for x in nums ]
                nums = [int(x) for x in nums ]
                matrix = np.array(nums)
                if i==1:
                    pts[0][0]=matrix[0]
                    pts[0][1]=matrix[1]
                    continue  
                pts=np.row_stack((pts, matrix))
                
             
            #pts = pts.reshape((-1,1,2))  
            img = cv2.fillConvexPoly(image,pts,color=(255,255,255))
            img2 = cv2.fillConvexPoly(image2,pts,color=(1,1,1))
            
            cv2.imwrite(new_nameM,img)
            cv2.imwrite(new_nameL,img2)
            print old_path
    
process_image('IM-0944-','F:/LV2009/label/SC-N-40/data/','F:/LV2009/label/SC-N-40/contours-manual/IRCCI-expert','F:/LV_data/')
