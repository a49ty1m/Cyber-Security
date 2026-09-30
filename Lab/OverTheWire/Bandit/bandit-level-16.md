# [Project] Bandit Level 16 — Short Title
**Target:** OverTheWire Bandit (level 16)  
**Author:** Aditya Mishra

## Executive summary
One-line: first use nmap to scan all the available ports between 31000 and 32000 then use ncat to hear between ssl connections in all the ports then you will key a ssh key then use it for level 

## Tools & methodology
Tools: ssh, ls, cat, file  
Method: connect via SSH → inspect files → read target file

## Findings / Solution
- **Goal:** retrieve password for next level  
 pass = kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

walkthrough
```
bandit16@bandit:~$ nmap localhost -p 31000-32000
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-10-16 09:41 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00012s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
bandit16@bandit:~$ man netcat | grep ssl
bandit16@bandit:~$ man ncat | grep ssl
                 --ssl                  Connect or listen with SSL
                 --ssl-cert             Specify SSL certificate file (PEM) for listening
                 --ssl-key              Specify SSL private key (PEM) for listening
                 --ssl-verify           Verify trust and domain name of certificates
                 --ssl-trustfile        PEM file containing trusted SSL certificates
                 --ssl-ciphers          Cipherlist containing SSL ciphers to use
                 --ssl-servername       Request distinct server name (SNI)
                 --ssl-alpn             ALPN protocol list to use
       --ssl (Use SSL)
       --ssl-verify (Verify server certificates)
           In client mode, --ssl-verify is like --ssl except that it also requires verification of the server certificate. Ncat comes with a default set of trusted certificates in the
           file ca-bundle.crt.  Some operating systems provide a default list of trusted certificates; these will also be used if available. Use --ssl-trustfile to give a custom list.
       --ssl-cert certfile.pem (Specify SSL certificate)
           --ssl-key.
       --ssl-key keyfile.pem (Specify SSL private key)
           This option gives the location of the PEM-encoded private key file that goes with the certificate named with --ssl-cert.
       --ssl-trustfile cert.pem (List trusted certificates)
           This option sets a list of certificates that are trusted for purposes of certificate verification. It has no effect unless combined with --ssl-verify. The argument to this
       --ssl-ciphers cipherlist (Specify SSL ciphersuites)
       --ssl-servername name (Request distinct server name)
       --ssl-alpn ALPN list (Specify ALPN protocol list)
           http://www.openssl.org

bandit16@bandit:~$ ncat --ssl localhost 31046 
Ncat: Input/output error.
bandit16@bandit:~$ ncat --ssl localhost 31518 
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx                                                                                                                                                      
^C
bandit16@bandit:~$ ncat --ssl localhost 31691
Ncat: Input/output error.
bandit16@bandit:~$ ncat --ssl localhost 31790 
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

exit
Ncat: Input/output error.
bandit16@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
smilo@smilo-LOQ-15AHP9:~$ nano key
smilo@smilo-LOQ-15AHP9:~$ ssh -i key bandit17@bandit.labs.overthewire.org -p 2220
