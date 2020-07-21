import argparse
import shutil
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--folder", required=True,
	help="folder to delete the content of")
args = vars(ap.parse_args())

folder = args["folder"]
Length = len([name for name in os.listdir(folder)])
i = 0
for filename in os.listdir(folder):
    i+=1
    print("DELETING {}".format(filename))
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
        
print("Press a key to continue !")
input()
