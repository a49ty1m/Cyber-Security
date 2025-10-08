# [Project] Bandit Level 13 — Short Title
**Date:** 2025-10-06  
**Target:** OverTheWire Bandit (level 13)  
**Time spent:** 20 min  
**Author:** Aditya Mishra

## Executive summary
One-line: use nc or netcat command it is use to connect between servers if you login as localhost at 30000 it will ask or password and will give the password for next level

## Tools & methodology
Tools: ssh, ls, cat, file  
Method: connect via SSH → inspect files → read target file

## Findings / Solution
- **Goal:** retrieve password for next level  
 pass = 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

walkthrough

bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 576FBDA199AABC5BBFCB018B6EF768060D26DE3625E2DE50687536F55ACA3AB5
    Session-ID-ctx: 
    Resumption PSK: 8698C297301F5682F7FA4169E624B7540409210F7686F30A501EB77D53E2782FBECD9D60F4594DD5B672D607C7763BAD
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - fa 01 fb 0b 54 e0 de c7-ec 9b 4d 60 6a 8e 77 d5   ....T.....M`j.w.
    0010 - 2a da e7 df 9a 62 cc de-35 b7 fa 81 ff 8b cb 7c   *....b..5......|
    0020 - 18 c2 b5 c2 8c 6d 5d 5a-90 c4 ea 6a bb 47 8a 47   .....m]Z...j.G.G
    0030 - 95 19 d2 5d 7f 08 38 e8-f7 dd 4d 7c 89 92 dc 3d   ...]..8...M|...=
    0040 - 04 c5 97 c2 48 90 a5 92-aa 11 3c bb 16 d2 85 b7   ....H.....<.....
    0050 - bc 7e 95 78 86 dc de 68-38 1e 8c af 00 74 19 29   .~.x...h8....t.)
    0060 - d7 d1 44 07 43 9f 91 eb-6a d9 50 45 98 0e 3d ec   ..D.C...j.PE..=.
    0070 - f1 31 20 a6 63 db 2b f4-8c da 24 90 87 42 03 a7   .1 .c.+...$..B..
    0080 - 5f 86 76 cd ec 48 66 a6-b1 9a d9 0c 2e 0f 61 9a   _.v..Hf.......a.
    0090 - cc ec 68 aa 64 22 2f 5d-2d 26 ab 82 3d a2 90 13   ..h.d"/]-&..=...
    00a0 - 8d c3 36 5c 7c 83 7d 4a-5c 5c 8f 3d 34 95 74 33   ..6\|.}J\\.=4.t3
    00b0 - ec a2 fc 77 24 a5 2f 65-57 e5 58 50 e5 da 18 24   ...w$./eW.XP...$
    00c0 - dc e3 d6 ba ca 3d fa a2-31 69 f3 14 24 bf 35 d7   .....=..1i..$.5.
    00d0 - 3f a3 64 e5 91 e7 fd 32-b0 b8 2e 95 6b a5 4e fe   ?.d....2....k.N.

    Start Time: 1759923206
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 9F3A1EE67B254A1C878F29DE7BEDAA88DF577A8CB658A1430024F996F8727186
    Session-ID-ctx: 
    Resumption PSK: 0BA9C9A8F21F3F293868B63B11B88124A5FCAD6B1E0FEBAB35BE3117BD524F1D88DC0B7114D948523B9289D2B68DA2F7
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - fa 01 fb 0b 54 e0 de c7-ec 9b 4d 60 6a 8e 77 d5   ....T.....M`j.w.
    0010 - ab 04 41 0e 5e c0 91 9a-c9 36 cf b1 a6 e8 b3 58   ..A.^....6.....X
    0020 - bb 0a 03 5a 38 81 89 5a-60 ca a5 ee a2 94 a9 67   ...Z8..Z`......g
    0030 - 0d 1e f0 55 a4 3b 48 fa-b0 db 74 b8 6d 96 e5 99   ...U.;H...t.m...
    0040 - bd e2 f4 6d 71 62 7e 36-03 2f 6f 8a 8f 09 bf 9a   ...mqb~6./o.....
    0050 - 41 79 67 3f 40 65 5f 86-3d 7d ae 9a 8f c6 11 2c   Ayg?@e_.=}.....,
    0060 - 1e d6 2d ea b1 ee 61 5c-b9 a5 dd 4f 57 10 04 d5   ..-...a\...OW...
    0070 - ad b0 64 39 ac ba 57 f1-60 c9 3d 79 b7 44 fc 1c   ..d9..W.`.=y.D..
    0080 - c7 b2 00 5e eb 43 c5 01-cc 38 cd 08 02 ff 6b 72   ...^.C...8....kr
    0090 - 0c 18 0a 94 d5 24 a7 d3-a8 e0 20 17 cb 53 88 9d   .....$.... ..S..
    00a0 - 6b 45 1d 68 fc 8c b8 9a-02 b3 09 90 03 38 8b 9d   kE.h.........8..
    00b0 - a1 29 c3 8d f0 c2 98 99-f7 c9 2d 36 1e ea fa 8a   .)........-6....
    00c0 - fe ed b4 1f 98 b1 bd 38-46 6b aa 71 d6 b1 da f6   .......8Fk.q....
    00d0 - 7e ed 25 3b 5d 30 4f 89-43 7e bb 59 1c 73 98 5e   ~.%;]0O.C~.Y.s.^

    Start Time: 1759923206
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

closed


