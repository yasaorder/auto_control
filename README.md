# auto_control
电脑端控制手机的一些程序

## 代码来源
https://github.com/mr-chen-king/auto_control_app
侵权即删

## get_phone_show
运行后实时获取手机画面，显示在电脑屏幕上

## 环境搭建

### 方法1. Windows 免添加配置 adb 环境变量方式

**注意**：如果你不想在 windows 下面配置 adb，也可以使用不需要配置的 adb 环境变量方式，但是需要在 Tool/adb 文件下操作，至于如何自动跳转，只需改变执行脚本即可，这里只做演示
 1. 将代码 clone 到本地后尝试把所有代码文件拷贝到 Tool/adb 文件夹下
 2. 在adb文件下操作：按住 shift + 右键 选择在该文件夹下打开命令窗口
 3. 打开安卓手机的 usb 调试，并连接电脑，在终端输入 `adb devices` 进行测试，如果有连接设备号则表示成功
 4. 打开get_phone_show，然后运行代码 `python get_phone_show.py`，然后屏幕左上角就会显示手机的实时画面
    

### 方法2. 手动配置 adb 到环境变量中
1. Android 或 Android 模拟器使用 ADB 进行连接
    - [ADB](https://developer.android.com/studio/releases/platform-tools.html) 驱动，可以到[这里](https://adb.clockworkmod.com/)下载
2. 如果你是 Android + macOS，请参考下面的配置：
    - 安装 Python 2.7/3
    - 使用 brew 进行安装 `brew cask install android-platform-tools`
    - 安装完后插入安卓设备且安卓已打开 USB 调试模式，终端输入 `adb devices` ，显示如下表明设备已连接
        ```
        List of devices attached
        6934dc33    device
        ```
    - 部分新机型可能需要再另外勾上**允许模拟点击**权限
    - 小米设备除了 USB 调试，还要打开底下的 USB 调试（安全）
    - USB 可能要设置成 MTP 模式
3. 如果你是 Android + Windows，请参考下面的配置：
    - 安装Python 2.7/3
    - 安装 [ADB](https://developer.android.com/studio/releases/platform-tools.html) 后，请在**环境变量**里将 adb 的安装路径保存到 PATH 变量里，确保 `adb` 命令可以被识别到
    - 同 Android + macOS 测试连接
4. 安装依赖文件
    ```shell
    pip install -r requirements.txt
    ```

### 操作步骤

1、安卓手机进入开发者模式，一般是 设置 > 关于本机 > 版本信息， 连续点击版本号5次
2. 安卓手机打开 USB 调试，设置 > 开发者选项 > USB 调试
3. 电脑与手机 USB 线连接，确保执行 `adb devices` 可以找到设备 ID
4. 界面打开小说软件
5. 进入项目目录，运行 `python get_phone_show.py` ，如果手机弹出界面显示 USB 授权，请点击确认
6. 请按照你的机型或手机分辨率从 `./config/` 文件夹找到相应的配置，把对应的 `config.json` 拷贝到项目根目录，与 *.py 同级
    - 如果屏幕分辨率能成功探测，会直接调用 config 目录的配置，不需要复制
    - 优先按机型去找，找不到再按分辨率
    - 如果都没有请找一个接近的自己的分辨率，或者调节一下找到合适的参数

## 二、iOS 手机操作步骤

> 可参考：[@神经嘻嘻兮兮：图文介绍iphone + macOS配置及操作](https://www.jianshu.com/p/ff973a5910ae)

### 环境安装

- 如果你是 iOS + macOS，请参考下面的配置
    - 使用真机调试 WDA，参考 iOS 真机如何安装 [WebDriverAgent · TesterHome](https://testerhome.com/topics/7220) 
    - 安装 [openatx/facebook-wda](https://github.com/openatx/facebook-wda)

- 安装依赖文件
    ```shell
    pip install -r requirements.txt
    ```
### 操作步骤

1. 运行安装好的 `WebDriverAgentRunner`
2. 将手机点击到小说界面
3. 界面打开小说软件
4. 进入项目目录，运行 `python get_phone_show.py` ，如果手机弹出界面显示 USB 授权，请点击确认
5. 请按照你的机型或手机分辨率从 `./config/` 文件夹找到相应的配置，把对应的 `config.json` 拷贝到项目根目录，与 *.py 同级
    - 如果屏幕分辨率能成功探测，会直接调用 config 目录的配置，不需要复制
    - 优先按机型去找，找不到再按分辨率
    - 如果都没有请找一个接近的自己的分辨率，或者调节一下找到合适的参数
