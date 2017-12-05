
# With Notepad++, use F5 then copy this into box
# C:\Python27\python.exe -i "$(FULL_CURRENT_PATH)"

import glob
import shutil
import os

dir_path = os.path.abspath(os.path.dirname(__file__))

src_dir = dir_path+os.sep+"iPhone Files"+os.sep
dst_dir = dir_path+os.sep+"All Photos"+os.sep

for jpgfile in glob.iglob(os.path.join(src_dir, "*/*.jpg")):
    if os.path.exists(dst_dir+os.path.basename(os.path.normpath(jpgfile))) == False:
		shutil.copy(jpgfile, dst_dir)

for movfile in glob.iglob(os.path.join(src_dir, "*/*.mov")):
    if os.path.exists(dst_dir+os.path.basename(os.path.normpath(movfile))) == False:
		shutil.copy(movfile, dst_dir)