# -*- coding: utf-8 -*-

"""
=== 思路 ===
核心：每次落稳之后截图，根据截图算出棋子的坐标和下一个块顶面的中点坐标，
    根据两个点的距离乘以一个时间系数获得长按的时间
识别棋子：靠棋子的颜色来识别位置，通过截图发现最下面一行大概是一条
    直线，就从上往下一行一行遍历，比较颜色（颜色用了一个区间来比较）
    找到最下面的那一行的所有点，然后求个中点，求好之后再让 Y 轴坐标
    减小棋子底盘的一半高度从而得到中心点的坐标
识别棋盘：靠底色和方块的色差来做，从分数之下的位置开始，一行一行扫描，
    由于圆形的块最顶上是一条线，方形的上面大概是一个点，所以就
    用类似识别棋子的做法多识别了几个点求中点，这时候得到了块中点的 X
    轴坐标，这时候假设现在棋子在当前块的中心，根据一个通过截图获取的
    固定的角度来推出中点的 Y 坐标
最后：根据两点的坐标算距离乘以系数来获取长按时间（似乎可以直接用 X 轴距离）
"""

import math
import re
import random
import sys
import threading
import time
from PIL import Image
from six.moves import input

if sys.version_info.major != 3:
    print('请使用Python3')
    exit(1)
try:
    from common import debug, config, screenshot, UnicodeStreamFilter
    from common.auto_adb import auto_adb
except Exception as ex:
    print(ex)
    print('请将脚本放在项目根目录中运行')
    print('请检查项目根目录中的 common 文件夹是否存在')
    exit(1)
adb = auto_adb()
VERSION = "1.1.4"

# DEBUG 开关，需要调试的时候请改为 True，不需要调试的时候为 False
DEBUG_SWITCH = False
adb.test_device()
# Magic Number，不设置可能无法正常执行，请根据具体截图从上到下按需
# 设置，设置保存在 config 文件夹中
config = config.open_accordant_config()
under_game_score_y = config['under_game_score_y']


def yes_or_no():
    """
    检查是否已经为启动程序做好了准备
    """
    while True:
        # yes_or_no = str(input('请确保手机打开了 ADB 并连接了电脑，'
        #                       '然后打开跳一跳并【开始游戏】后再用本程序，确定开始？[y/n]:'))
        yes_or_no = 'y'
        if yes_or_no == 'y':
            break
        elif yes_or_no == 'n':
            print('谢谢使用', end='')
            exit(0)
        else:
            print('请重新输入')


import tkinter as tk
from PIL import Image, ImageTk


def open_image_window(image, window_width, window_height, window_x, window_y,img_is_path=False):
    """
    在指定位置创建一个指定大小的窗口，打开图片
    image可以是路径，也可以是 PIL 对象
    """
    # 创建窗口
    window = tk.Tk()
    window.title("Image Viewer")
    window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    while True:
        im = screenshot.pull_screenshot()
        photo = update_img(im, window_width=window_width, window_height=window_height)

        label = tk.Label(window, image=photo)
        label.grid(row=1, column=0)
        window.update()
        window.after(10)

    # Start the loop in a separate thread
    # loop_thread = threading.Thread(target=loop(window))
    # loop_thread.daemon = True
    # loop_thread.start()

    window.mainloop()


def update_img(image, window_width, window_height):
    # image = image.resize((window_width, window_height), Image.ANTIALIAS)
    # 最新版 pillow 删除了ANTIALIAS 方法, 可修改为 LANCZOS
    if image.load():
        image = image.resize((window_width, window_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        return photo

    else:
        print("图片未加载")


def main():
    """
    主函数
    """
    print('程序版本号：{}'.format(VERSION))
    print('激活窗口并按 CONTROL + C 组合键退出')
    debug.dump_device_info()
    screenshot.check_screenshot()

    # im = screenshot.pull_screenshot()

    open_image_window(screenshot, 180, 240, 0, 0)


if __name__ == '__main__':
    try:
        yes_or_no()
        main()
    except KeyboardInterrupt:
        adb.run('kill-server')
        print('\n谢谢使用', end='')
        exit(0)
