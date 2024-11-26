
import time
import ctypes
from ctypes import *  # 导入 ctypes 库中所有模块
keyBoardCode = {
    'up' : 82,
    'down' : 81,
    'left' :80,
    'right' : 79,
    'q' : 20,
    'w' :26,
    'e' : 8,
    'r' :21,
    'j' : 13,
    'x' : 27

}
objdll = ctypes.windll.LoadLibrary('./msdk.dll')
hdl = objdll.M_Open(1)

#敲击按键
def keyPress(input):
    global hdl
    # 键盘单击    # 键盘敲击a（4）两次
    res = objdll.M_KeyPress(hdl,keyBoardCode[input],1)  # 打开

#按下按键不松手
def keyDown(input):
    global hdl
    # 键盘单击    # 键盘敲击a（4）两次
    res = objdll.M_KeyDown(hdl, keyBoardCode[input])
#放开按键
def keyUp(input):
    global hdl
    print("open handle = " + str(hdl))
    # 键盘单击    # 键盘敲击a（4）两次
    res = objdll.M_KeyUp(hdl, keyBoardCode[input])  # 打开

#复位M_ReleaseAllKey
def releaseAllKey():
    global hdl
    res = objdll.M_ReleaseAllKey(hdl)
