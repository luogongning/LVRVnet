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
def process_image(dir_Path):
    
    for root,dirs,files in os.walk(dir_Path):
        subdir_split = root.split('/')
        print subdir_split[3]
        for fileobj in files:
            
            a=fileobj.replace('L','');
            print a
            print fileobj
            oldname=dir_Path+fileobj
            newname= dir_Path+a
            print oldname
            print newname
            os.rename(oldname,newname)
    
process_image('F:/LV2009_segmentation/LV_Label/')