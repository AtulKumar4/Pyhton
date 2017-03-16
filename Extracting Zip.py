from os.path import join
from os import listdir, rmdir
from shutil import move
import zipfile,fnmatch,os, re
from glob import glob
import shutil
rootPath = 'C:/Users/akumar4/Desktop/script/'
pattern = '*.zip'

for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
        zipfile.ZipFile(os.path.join(root,     filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))


for root, dirs, files in os.walk(rootPath):
    for f in files:
        if f.endswith(".zip"):
            os.unlink(os.path.join(root, f))
path = 'C:/Users/akumar4/Desktop/script/'

for path, sub_directories, files in os.walk(path):
    directory_name = os.path.split(path)[1]

    for file in files:
        extension = os.path.splitext(file)[1]
        source = os.path.join(path, file)
        destination = os.path.join(path, directory_name+extension)
        os.rename(source, destination)		
  
import os, shutil, sys 

def move_to_root_folder(root_path, cur_path):
    for filename in os.listdir(cur_path):
        if os.path.isfile(os.path.join(cur_path, filename)):
            shutil.move(os.path.join(cur_path, filename), os.path.join(root_path, filename))
        elif os.path.isdir(os.path.join(cur_path, filename)):
            move_to_root_folder(root_path, os.path.join(cur_path, filename))
        else:
            sys.exit("Should never reach here.")
    # remove empty folders
    if cur_path != root_path:
        os.rmdir(cur_path)

move_to_root_folder(os.getcwd(),os.getcwd())		
