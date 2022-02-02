import requests
import os
import argparse

print("===Link Checker Tool===\n")

#adding and parsing arguments
parser=argparse.ArgumentParser()
parser.add_argument("filename",help="Filename or filepath")
parser.add_argument("-o","--output", help="Save result in a output a new file. '-o filename.txt'")
args = parser.parse_args()


#Filename/path check
if (os.path.isfile(args.filename))==False:
    print("Invalid File Name or file not found")
    exit()

#open file and store its content in variable
f=open(args.filename,"r")
data=f.read()

#Converting file contents into list.
data=data.split("\n")

#looping through each list item and printing results.
result=""
status_code=""

#opening output file in write mode if -o argument is provided
if args.output:
    xd=open(args.output,"w")

#function if output is not selected
def on_screenFunc():
        for x in data:
            try:
                r=requests.get(x,timeout=3)
                status_code=r.status_code

                result=f"{x} :{status_code}"
                print(result)
            except:
                 result=f"{x}: Unable to connect."
                 print(result)


#function if output is selected
def outputFunc():
    for x in data:
        try:
            r = requests.get(x, timeout=3)
            status_code = r.status_code

            result = f"{x} :{status_code}\n"
            xd.write(result)
            print(result)
        except:
            result = f"{x}: Unable to connect.\n"
            xd.write(result)
    print(f"Results has been saved to '{args.output}' file")
#if -o argument is provided
if args.output:
    outputFunc()

#if -o argument is not provided
else:
    on_screenFunc()

#Closing opened file.
f.close()
