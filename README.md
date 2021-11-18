# Wordpress-420



- Exploit Title: Wordpress Plugin Smart Product Review 1.0.4 - Arbitrary File Upload
-Google Dork: inurl: /wp-content/plugins/smart-product-review/
-Exploit Author: Keyvan Hardani
-usage python3 Auto-wp.py www.example.com your Shell.php4/phtml





# Wordpress user enumeration and password bruteforce.

#User Enumeration:

usage: python2 wp-b.py -t [target] -u [user] -w [passlist]

optional arguments:

  -h, --help   How User This Tool
 
 -t TARGET    For Example : localhost/wordpress/wp-login.php
  
-u USER      username 0f Target
 
 -w PASSLIST  address passlist for brute force
 
 -r           Restore the last session of the attack


# Example
python2 wp-b.py-t www.site.com/wp-login.php -u Admin -w wordlist.txt


More coming soon 😴
