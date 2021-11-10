# Wordpress-Bruteforce



Wordpress user enumeration and password bruteforce.

#User Enumeration:

usage: python2 wp.py -t [target] -u [user] -w [passlist]

optional arguments:

  -h, --help   How User This Tool
 
 -t TARGET    For Example : localhost/wordpress/wp-login.php
  
-u USER      username 0f Target
 
 -w PASSLIST  address passlist for brute force
 
 -r           Restore the last session of the attack


# Example
python2 wp.py-t www.site.com/wp-login.php -u Admin -w wordlist.txt
