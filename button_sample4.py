#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 説明を表示する
print("--------------------------------------------------------------")
print("○  ボタンの組み合わせによってドアが開閉します。")
print("○  ボタンの入力は「0」か「1」を半角でキーボード入力します。")
print("--------------------------------------------------------------")

# ボタン1の入力を受け付けて、結果をbutton1に保存
button1 = int(raw_input("ボタン1を入力 > "))
# ボタン2の入力を受け付けて、結果をbutton2に保存
button2 = int(raw_input("ボタン2を入力 > "))
# ボタン3の入力を受け付けて、結果をbutton3に保存
button3 = int(raw_input("ボタン3を入力 > "))
print("---------------------------")

# ボタン1、ボタン2、ボタン3が押されているか判定する
if button1 == 1 and button2 == 1 and button3 == 1:
    print("=>ドアが開きました。")
# ボタン1、ボタン2、ボタン3が押されていないか判定する
elif button1 == 0 and button2 == 0 and button3 == 0:
    print("=>ドアが開きませんでした。")
# 上2つの条件に当てはまらないとき、ボタンが足りないというメッセージを出す
else:
    print("=>ドアを開けるにはボタンが足りませんでした。")