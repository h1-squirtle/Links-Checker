# Links-Checker
Tool which lets you check HTTP status code of links from a file. Results can be seen on screen and can be saved to a file. 

**1. Output shown on screen:**
--
```
python linkschecker.py <filename-containing-links>
```

**Expected output:**
```
https://baseurl.com: 200
https://baseurl.com: 404
https://baseurl.com: 500
https://baseurl.com: Unable to conenct
```

**2. Save output to file:**
--
```
python linkschecker.py <filename-containing-links> -o newFileName.txt
```

**Expected output:**
```
Results has been stored to 'output' file.
```
Future work:
--
1. Add multithreading to run multiple requests at a time to reduce time.
