import cv2
import numpy as np
import geojsoncontour
import matplotlib.pyplot as plt
import json
import os

# =============================================================================
# path = r"C:\Users\acatg\TRAINING\ISKEMI\MASK\\"
# 
# a = cv2.imread(path + "10053.png",cv2.IMREAD_UNCHANGED)
# 
# 
# img_grey = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(img_grey, 25, 255, 0)
# cv2.imwrite(r"C:\Users\acatg\Downloads\3.png",thresh)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 
# isClosed = True
#   
# # Blue color in BGR
# color = (0, 0, 255)
#   
# # Line thickness of 2 px
# thickness = 1
#   
# # Using cv2.polylines() method
# # Draw a Blue polygon with 
# # thickness of 1 px
# 
# c = np.zeros((a.shape[0],a.shape[1],3))
# 
# for i in range(len(contours)):
#     
#     c = cv2.polylines(c, [contours[i]], 
#                       isClosed, color, thickness)
#     
# cv2.imwrite(r"C:\Users\acatg\Downloads\4.png",c)
# =============================================================================

img_dir = r"C:/Users/emine/MASK/MASK/"
data_path = os.listdir(img_dir) 
data = [] 
contours_list = []          # koordinatlar tutuluyor
images_paths_list = []      # dosya yolları tutuluyor
images_size_list = []       # dosya size'ları tutuluyor
with os.scandir("C:/Users/emine/MASK/MASK/") as file:
    for img_size in file:
        print(img_size.name,"isimli görüntü size(Byte): ",os.stat(img_size).st_size)
        a = os.stat(img_size).st_size
        images_size_list.append(a) 
      
for f1 in data_path: 
    images_paths_list.append(f1)
    img = cv2.imread(img_dir+f1)
    img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_grey, 25, 255, 0)
    cv2.imwrite(r"C:/Users/emine/test.png",thresh)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_list.append(contours)
    data.append(img) 

all_string = "{"
for index,path in enumerate(data_path):
    if(index==571):
        break
    ## filename
    filename = path
    filename_string = "\"filename\":" + "\"" + filename + "\""
    
    ## size
    size = str(images_size_list[index])
    size_string = "\"size\":" + size 
    
    regions = "["
    
    for each in contours_list[index]:        
        name = "\"polygon\""
        name_string = "\"name\":" + name
        
        x = each[:,:,0]
        y = each[:,:,1]

        x = x.reshape(x.shape[0])
        y = y.reshape(y.shape[0])
        
        all_points_x = "["
        all_points_y = "["
        for j in range(len(x)):
            all_points_x = all_points_x  + str(x[j]) + ","
            all_points_y = all_points_y  + str(y[j]) + ","
            
        all_points_x = all_points_x[:len(all_points_x) -1] + "]"
        all_points_y = all_points_y[:len(all_points_y) -1] + "]"
        
        all_points_x_string = "\"all_points_x\":" + str(all_points_x)
        
        all_points_y_string = "\"all_points_y\":" + str(all_points_y)
        
        shape_attributes = "{" + name_string + "," + all_points_x_string + "," + all_points_y_string + "}"
        shape_attributes_string = "\"shape_attributes\":" + shape_attributes
        
        
        names = "\"iskemik\""
        names_string = "\"names\":" + names
        
        region_attributes = "{" + names_string + "}"
        region_attributes_string = "\"region_attributes\":" + region_attributes
        
        regions_element = "{" + shape_attributes_string +"," + region_attributes_string + "}"
        regions = regions + regions_element + ","
     
    regions = regions[:len(regions)-1] + "]"
    regions_string = "\"regions\":" + regions
    
    ##file_attributes
    file_attributes = "{}"
    file_attributes_string = "\"file_attributes\":" + file_attributes
    
    ##image
    image = "{" + filename_string +"," + size_string + "," + regions_string + "," + file_attributes_string + "}"
    image_string = "\"" + filename + size +"\":" + image
    
    all_string += image_string + ","

all_string = all_string[:len(all_string)-1] + "}"












