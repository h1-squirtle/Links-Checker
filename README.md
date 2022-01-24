# Links-Checker
Tool which lets you check HTTP status code of links from a file. Results will be printed on screen.

**Syntax:**

python linkschecker.py \<filename-containing-links\>

**Expected output:**

`https://baseurl.com  <statuscode>`

`https://baseurl.com   200`

Future work:
--
1. Add option to let user save results to a file.
2. Add multithreading to run multiple requests at a time to reduce time.
