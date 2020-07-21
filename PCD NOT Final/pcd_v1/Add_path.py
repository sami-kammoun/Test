import argparse
import shutil
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ptyf", required=True,
	help="path to copy the images from")
ap.add_argument("-e", "--ctp", required=True,
	help="path to copy the images to")
args = vars(ap.parse_args())

path_to_your_files = args["ptyf"]
copy_to_path = args["ctp"]
        
##'destination for your copy'
if not os.path.exists(copy_to_path):
    os.makedirs(copy_to_path)
            
files_list = sorted(os.listdir(path_to_your_files))
orders = range(0, len(files_list))
i=0
for order in orders:
    i+=1
    files = files_list[order]
    print("Copying {} : {}/{}".format(files,i,len(files_list)))
    shutil.copyfile(os.path.join(path_to_your_files, files), os.path.join(copy_to_path, files))  # copying images to destination folder
print("Copying Done !")
input()
