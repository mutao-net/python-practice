# -*- coding: utf-8 -*-
import os
# ディレクトリが存在しなければ作成する
direcory_path = "./target/"
if not os.path.exists(direcory_path):
    os.mkdir(direcory_path)

# 外部ファイルの読み込み
f = open("client.json", "r")
client_info = json.load(f)
f.close()