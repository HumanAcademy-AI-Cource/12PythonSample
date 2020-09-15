#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 説明を表示する
print("--------------------------------------------------------------")
print("○  センサデータを入力すると目の前に障害物があるか検出します。")
print("--------------------------------------------------------------")

# センサデータを入力する
sensor_data = int(raw_input("センサデータ入力(mm) > "))
print("---------------------------")

# センサデータが100mm以下の場合
if sensor_data <= 100:
    print("=>目の前に障害物があります。")
# センサデータが100mmより大きい場合
if sensor_data > 100:
    print("=>目の前には何もありません。")
