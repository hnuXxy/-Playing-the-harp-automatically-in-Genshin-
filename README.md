# -Playing-the-harp-automatically-in-Genshin-
实现原神自动弹琴的python脚本（Implementation of the Genshin automatic  playing harp Python script）
## 环境准备
1、如果电脑没有python环境先安装python3以上版本(或Anaconda，建议还是安装python)
2、安装python库pyautogui，使用命令行：
```Shell
pip install pyautogui
```
Anaconda如果上述命令不可行则使用：
```Shell
conda install pyautogui
```

## 运行
1、打开原神，拿出乐器
2、脚本需要以管理员身份运行，找到Windows PowerShell，右键以管理员身份运行
3、使用cd命令转到下载autoplay.py的文件夹：
```Shell
cd 'path'
```
path就是autoplay.py所在的目录，注意Windows下路径需要用单引号‘ ‘
4、在该目录下使用python命令运行脚本：
```Shell
python autoplay.py
```
5、然后有五秒钟的时间，此时进入原神等待即可

## 扩展
可以自己在程序里面添加想要弹奏的歌曲乐谱（b站有很多），然后将toPlay改为要演奏的歌曲，再自己调节一下节奏即可（代码中均有注释）



## -   Environment to prepare
1. If your computer does not have a Python environment, install Python3 or later (or Anaconda, it is recommended to install Python).
2. Install the Python library Pyautogui using the command line:
```Shell
pip install pyautogui
```
Anaconda If the above command is not feasible:
```Shell
conda install pyautogui
```

## Operation
1. Open Genshin and take out the instrument
2. The script needs to be run as an administrator. Find Windows PowerShell and right click to run as an administrator
3. Use the 'cd' command to go to the folder where autoplay. py was downloaded:
```Shell
cd 'path'
```
Path is the directory where autoplay.py is located. Note that on Windows, the path requires single quotation marks (').
4. Run the script from this directory using the python command:
```Shell
python autoplay.py
```
5. and then have five seconds, this time into the Genshin can wait

## Extension
You can add the music you want to play in the program (there are many in www.bilibili.com), then change ***toPlay*** to the music you want to play, and then adjust the rhythm by yourself (there are comments in the code).
