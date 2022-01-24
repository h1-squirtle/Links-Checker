import requests
import sys
import os

print("===LinkChecker v1===\n")

#Filename/path check
if (os.path.isfile(sys.argv[1]))==False:
    print("File not found/Filename incorrect.\nSyntax: 'python linkchecker.py <filename>'\n")
    sys.exit()

#open file and store its content in variable
f=open(sys.argv[1],"r")
data=f.read()

#Converting file contents into list.
data=data.split("\n")

status_code=""
#looping through each list item and printing results.
for x in data:
    try:
        r=requests.get(x,timeout=3)
        status_code=r.status_code
        print(x,": ",status_code)
    except :
        print(x,": Unable to connect.")

f.close()