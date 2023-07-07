# Python program to explain os.mkdir() method
  
# importing os module
import os
  
# Directory
directory = "Roblox_Mass_Report_main_FIXED_ON_ID"
  
# Parent Directory path
parent_dir = "%userprofile%\Downloads\files_in_usage"
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)
  
# Directory
directory = "Geeks"
  
# Parent Directory path
parent_dir = "D:/Pycharm projects"
  
# mode
mode = 0o666
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)
h = input("lol")
