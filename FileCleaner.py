# FileCleaner.py

# With Notepad++, use F5 then copy this into box
# C:\Python27\python.exe -i "$(FULL_CURRENT_PATH)"

# -------------------------------------------------
# IMPORTS
# -------------------------------------------------

import glob
import shutil
import os
import exifread
# import re
import Image


# -------------------------------------------------
# DEFINE FUNCTIONS
# -------------------------------------------------

# Define last position finder
def find_last(s,t):
	last_pos = -1
	while True:
		pos = s.find(t, last_pos +1)
		if pos == -1:
			return last_pos
		last_pos = pos

# -------------------------------------------------
# INPUTS
# -------------------------------------------------

dir_path = os.path.abspath(os.path.dirname(__file__))

# src_dir = dir_path+os.sep+"iPhone Files"+os.sep
# copy_dir = dir_path+os.sep+"All Photos"+os.sep
# dst_dir = dir_path+os.sep+"Timestamped"+os.sep

# Name base folder
base = '2015'

src_dir = dir_path+os.sep+base+os.sep
copy_dir = dir_path+os.sep+base+" Copy"+os.sep
dst_dir = dir_path+os.sep+base+"- Timestamped"+os.sep

# src_dir = dir_path+os.sep+"Timestamped"+os.sep+"Not Stamped"+os.sep
# copy_dir = dir_path+os.sep+"Timestamped"+os.sep+"Copied"+os.sep
# dst_dir = dir_path+os.sep+"Timestamped"+os.sep+"Timestamped"+os.sep

# -------------------------------------------------
# OPERATIONS
# -------------------------------------------------

# Extract from file structure
# -------------------------------------------------

for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
# for jpgfile in glob.iglob(os.path.join(src_dir, "*/*.jpg")):
    if os.path.exists(copy_dir+os.path.basename(os.path.normpath(jpgfile))) == False:
		print('Copying '+jpgfile[find_last(jpgfile,os.sep)+1:])
		shutil.copy(jpgfile, copy_dir)

for pngfile in glob.iglob(os.path.join(src_dir, "*.PNG")):
# for jpgfile in glob.iglob(os.path.join(src_dir, "*/*.jpg")):
    if os.path.exists(dst_dir+os.path.basename(os.path.normpath(pngfile))) == False:
		print('Copying '+pngfile[find_last(pngfile,os.sep)+1:])
		shutil.copy(pngfile, dst_dir)

for movfile in glob.iglob(os.path.join(src_dir, "*.mov")):
# for movfile in glob.iglob(os.path.join(src_dir, "*/*.mov")):
    if os.path.exists(dst_dir+os.path.basename(os.path.normpath(movfile))) == False:
		print('Copying '+movfile[find_last(movfile,os.sep)+1:])
		shutil.copy(movfile, dst_dir)
		
for mp4file in glob.iglob(os.path.join(src_dir, "*.mp4")):
# for movfile in glob.iglob(os.path.join(src_dir, "*/*.mov")):
    if os.path.exists(dst_dir+os.path.basename(os.path.normpath(mp4file))) == False:
		print('Copying '+mp4file[find_last(mp4file,os.sep)+1:])
		shutil.copy(mp4file, dst_dir)

# Move and rename files
# -------------------------------------------------

# Get file list including iPhone, CanonPowerShot, and Nikon1 files
Files = glob.glob(copy_dir+"*.jpg")
# Open array to build dictionary
result = range(len(Files))

# Open loop to treat each jpg file
for i in range(len(Files)):
	
	# Open image file
	img = Image.open(Files[i])
	# Get date information by getting minimum creation time
	exif_data = img._getexif()
	mtime = "?"
	if 306 in exif_data and exif_data[306] < mtime: # 306 = DateTime
		mtime = exif_data[306]
	if 36867 in exif_data and exif_data[36867] < mtime: # 36867 = DateTimeOriginal
		mtime = exif_data[36867]
	if 36868 in exif_data and exif_data[36868] < mtime: # 36868 = DateTimeDigitized
		mtime = exif_data[36868]
	
	# Add "_" for each repeat of exact time
	j = 0
	while mtime+"_"*j in result:
		j += 1
	mtime = mtime+"_"*j
	result[i] = mtime
	
	# Determine if it has relevant date information and assign name
	if '?' in result[i]:
		newName = Files[i][find_last(Files[i],os.sep)+1:-4]
	else:
		newName = result[i][:result[i].find(' ')].replace(":", "-") + result[i][result[i].find(' '):].replace(":", "")
	# print(newName+', '+exif_data)
	
	# Copy files to new directory with new name
	if os.path.exists(dst_dir+newName+'.jpg') == False:
		print('Copying '+newName+'.jpg')
		shutil.copy2(Files[i], dst_dir+newName+'.jpg')

