#! /usr/bin/python3
from subprocess import call
import os.path
import os
import time;
import sys

TEMP_FILE_PATH = "/tmp/downloader.tempfile"


# If temp file exists, don't do anything
if os.path.isfile(TEMP_FILE_PATH):
    print("tempfile exists")
    sys.exit()

# Otherwise...

# Write temp file
tempFile = open(TEMP_FILE_PATH, "w+")
tempFile.write(time.asctime(time.localtime(time.time())))
tempFile.close()

# Run commands
with open('toDownload.txt', 'r') as f:
    for line in f:
        print(call(line.strip().split(" ")))

# Clear file, because all lines done
with open('toDownload.txt', 'w') as f:
    f.write("")

# When done, delete temp file
os.remove(TEMP_FILE_PATH)
