# File Name: declutter.py
import os
print ('Welcome to the declutter program!')
print ('This program will help you declutter your folder by renaming files.')
print ('You can choose the file type you want to declutter.')
print ('For example: png, jpg, pdf, etc. (without the dot)')
print ('Just copy and paste the folder path where your files are located.')
print ('Please make sure to enter the correct file type and folder path.')

user_filetype  = input('Enter the filetype you want to declutter: ')
user_filetype = '.' + user_filetype.strip().lower()
user_folderpath = input('Enter the folder path: ')
user_folderpath = user_folderpath.strip()
def declutter(folder_path, file_type):
   counter = 1
   os.chdir(folder_path)
   files = os.listdir(folder_path)
   for file in files:
      if file.endswith(file_type):
         os.rename(file, str(counter) + file_type)
         counter += 1
         print(f'{file} renamed to {counter - 1}{file_type}')
         print('All files have been renamed successfully!')
      else: 
         print('Invalid input. Please check the file type and folder path.')
         break
declutter(user_folderpath, user_filetype)


