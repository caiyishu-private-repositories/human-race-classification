import numpy as np
import cv2
import random
import os
import argparse

## function of resizing image with border replicate
def resize(image, new_height, new_width):
    height = image.shape[0]
    width = image.shape[1]
    print('Resizing from (' + str(height) + ', ' + str(width) +  ') to (' + str(new_height) + ', ' + str(new_width) + ')')
    
    m = max(height, width)
    res_height = int((m-height)/2)
    res_width = int((m-width)/2)
    ##print("res_height", res_height)
    ##print("res_width", res_width)

    resized = cv2.copyMakeBorder(image, res_height, res_height, res_width, res_width, cv2.BORDER_REPLICATE)
    resized = cv2.resize(resized, (new_width, new_height))
    return resized

## function returns list of all files in directory
def get_files(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + get_files(fullPath)
        else:
            allFiles.append(fullPath)     
    return allFiles

## 
## MAIN
##
if __name__=="__main__":

    # parse params
    args = argparse.ArgumentParser()
    args.add_argument("-p", "--path", type=str, help="Relative or absolute path", required=False)
    args.add_argument("-c", "--height", type=int, help="New height", required=True)
    args.add_argument("-r", "--width", type=int, help="New width", required=True)
    args = args.parse_args()

    # set params
    new_height = args.height
    new_width = args.width
    path = args.path
    if path is None: path = '' # current directory

    # constants
    formats = ['jpeg', 'jpg', 'png', 'bmp']

    print('Starting program...')
    print('Supported formats ', formats)
    root_dir = os.getcwd()
    current_dir = os.path.join(root_dir, path)
    print('Directory: ', current_dir)
    files = get_files(current_dir)
    counter = 0

    for file in files:
        if file.split('.')[-1].lower() in formats:
            print(file)
            try:
                image = cv2.imread(file)
                image = resize(image, new_height, new_width)
                cv2.imwrite(file,image)
            except Exception as e:
                print(e)
            counter += 1
            
    print('Total number of processed files: ' + str(counter))
    print('Done')
