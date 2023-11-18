# -*- coding: utf-8 -*-
import os
import subprocess
import platform


class auto_adb():
    """
    auto_adb`类用于自动检测并启动ADB工具。它有以下功能：

    1. 初始化`auto_adb`类时，尝试启动ADB工具。
    2. 如果ADB无法启动，根据操作系统分别查找ADB的可执行文件路径。
    3. 如果仍无法启动ADB，提示用户安装ADB及驱动并配置环境变量。
    """
    def __init__(self):
        try:
            adb_path = 'adb'
            subprocess.Popen([adb_path], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
            self.adb_path = adb_path
        except OSError:
            if platform.system() == 'Windows':
                adb_path = os.path.join('Tools', "adb", 'adb.exe')
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    self.adb_path = adb_path
                except OSError:
                    pass
            else:
                try:
                    subprocess.Popen(
                        [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except OSError:
                    pass
            print('请安装 ADB 及驱动并配置环境变量')
            print('具体链接: https://github.com/wangshub/wechat_jump_game/wiki')
            exit(1)

    def get_screen(self):
        """
        这个方法通过ADB在设备上运行 `wm size` 命令，
        获取并返回设备屏幕的大小信息。它首先使用 `os.popen` 创建一个子进程来执行ADB命令，然后读取命令的输出。
        """
        process = os.popen(self.adb_path + ' shell wm size')
        output = process.read()
        return output

    def run(self, raw_command):
        """
        这个方法接收一个原始的ADB命令作为输入，然后创建一个新的子进程来执行这个命令，最后返回命令的输出结果。
        """
        command = '{} {}'.format(self.adb_path, raw_command)
        process = os.popen(command)
        output = process.read()
        return output

    def test_device(self):
        """
        这个方法检查是否有一个设备连接到了ADB。
        它首先创建一个子进程来运行 `adb devices` 命令，然后解码输出结果，检查结果是否包含文本 "List of devices attached"。
        如果包含这个文本，说明有设备连接；
        如果不包含，则说明没有设备连接。无论结果如何，该方法都会打印出ADB的输出，并在有设备连接的情况下退出程序。
        """
        print('检查设备是否连接...')
        command_list = [self.adb_path, 'devices']
        process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()
        if output[0].decode('utf8') == 'List of devices attached\n\n':
            print('未找到设备')
            print('adb 输出:')
            for each in output:
                print(each.decode('utf8'))
            exit(1)
        print('设备已连接')
        print('adb 输出:')
        for each in output:
            print(each.decode('utf8'))

    def test_density(self):
        """
        该函数用于获取设备屏幕的密度。它通过在设备上运行 `adb shell wm density` 命令来获取屏幕密度，并将结果显示在输出中。
        """
        process = os.popen(self.adb_path + ' shell wm density')
        output = process.read()
        return output

    def test_device_detail(self):
        """
        该函数用于获取设备的详细信息。
        它通过在设备上运行 `adb shell getprop ro.product.device` 命令来获取设备型号，并将结果显示在输出中。
        """
        process = os.popen(self.adb_path + ' shell getprop ro.product.device')
        output = process.read()
        return output

    def test_device_os(self):
        """
        该函数用于获取设备操作系统的版本。
        它通过在设备上运行 `adb shell getprop ro.build.version.release` 命令来获取操作系统版本，并将结果显示在输出中。
        """
        process = os.popen(self.adb_path + ' shell getprop ro.build.version.release')
        output = process.read()
        return output

    def adb_path(self):
        return self.adb_path
