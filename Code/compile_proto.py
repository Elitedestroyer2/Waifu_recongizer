import os
import sys
args = sys.argv
directory = 'models/research/object_detection/protos'
protoc_path = 'C:/Codeing/protoc/bin/protoc.exe'
for file in os.listdir(directory):
    if file.endswith(".proto"):
        os.system('protoc' +" "+directory+"/"+file+" --python_out=.")
 