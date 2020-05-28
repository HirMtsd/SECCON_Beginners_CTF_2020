# coding: utf-8
# 2020/05/24 @HirMtsd
# Code for 'SECCON Beginners CTF 2020'

# 答えの準備
a = ""

# emoemoencode.txtをバイナリで読み込み
with open("emoemoencode.txt", "rb") as f:
    # 初回読み込み
    c = f.read(4)

    # ファイルの終わりまでループ
    while c[0] != b"" and c[0] != 0x0a:
        # 3バイト目が0x8Cの場合、4バイト目から0x80を引く
        if c[2] ==0x8c:
            a += chr(c[3] - 0x80)
        # 3バイト目が0x8Dの場合、4バイト目から0x40を引く
        elif c[2] == 0x8d:
            a += chr(c[3] - 0x40)

        # ループ読み込み
        c = f.read(4)

    # 答え出力
    print(a)
