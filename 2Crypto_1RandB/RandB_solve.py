# coding: utf-8
# 2020/05/24 @HirMtsd
# Code for 'SECCON Beginners CTF 2020'

import codecs
import base64

# シーザー暗号復号
def rot13_(s):
    return codecs.decode(s, 'rot13')

# Base64復号
def base64_(s):
    return (base64.b64decode(s.encode())).decode()

# 符号化データ
with open("r_and_b\encoded_flag") as f:
    enc = f.readline()

# ループ
while True:
    print(enc)
    if not (enc[0] == "B" or enc[0] == "R"):
        break
    else:
        if enc[0] == "B":
            enc = base64_(enc[1:])
        elif enc[0] == "R":
            enc = rot13_(enc[1:])

print("FLAG:")
print(enc)
