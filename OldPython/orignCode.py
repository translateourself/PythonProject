# from pydoc_data.topics import topics
#
# import cv2
# import mss
# import numpy as np
# import ctypes
# import string
# import time
# from ctypes import *  # 导入 ctypes 库中所有模块
#
# import judgeScene
# import getObjectLocation
#
# # defined screen capture area
#  # left 表示距离屏幕左边界多少像素
# #  top 截图距离上边界多少像素
# # width 截图的宽度
# # height 截图的高度
# CaptureArea = {"left" :0, "top":0, "width" : 800, "height" : 600 }
# #场景列表
# scene = ["GameStart.png","sailiya.png","Town.png"]
#
#
#
#
# # //  实例化mss
# with mss.mss() as sct:
#   while True :
#     currentScene = "未知"
#     character_Location = (0,0)
#     #获取截屏
#     ScreenCapture = sct.grab(CaptureArea)
#     ScreenCapture = np.array(ScreenCapture)
#     # 大部分图片查找时候根据形状和样子来查找，和颜色没有差距。所以转成灰度图片后查找更快
#     # opcv 提供将图片转换为灰度的方法
#     bigPicture_gray = cv2.cvtColor(ScreenCapture,cv2.COLOR_BGR2RGB)
#
#     # 获取场景代码
#     for currentScene in scene:
#     # opcv 提供加载图片的方法
#       smallPicture =  cv2.imread(currentScene)
#       smallPicture_gray = cv2.cvtColor(smallPicture,cv2.COLOR_BGR2RGB)
#
#       # opcv提供在大图片中找小图片的方法
#       result = cv2.matchTemplate(bigPicture_gray,smallPicture_gray,cv2.TM_CCOEFF_NORMED)
#
#       locations =np.where(result >= 0.85) #使用np筛选相似度大于等于0.85的
#       locations = list(zip(*locations[::-1])) #再次处理仅保留坐标
#
#       if len(locations) > 0 :
#         if "GameStart" in currentScene:
#           print("当前在角色选择画面", locations)
#         elif "sailiya" in currentScene:
#             objdll = ctypes.windll.LoadLibrary('./msdk.dll')
#             hdl = objdll.M_Open(1)
#             print("open handle = " + str(hdl))
#             time.sleep(3)  # sleep 3s 加延时，延时期间将鼠标点到记事本里，方便调试用
#             # 键盘单击
#             # 键盘敲击a（4）两次
#             res = objdll.M_KeyPress(hdl, 4, 2)  # 打开
#             print("当前在赛利亚房间", locations)
#         elif "Town" in currentScene:
#           print("当前在城镇", locations)
#         break
#
#     #获取角色坐标代码
#     smallPicture = cv2.imread("Character.png")
#     smallPicture_gray = cv2.cvtColor(smallPicture, cv2.COLOR_BGR2RGB)
#
#     # opcv提供在大图片中找小图片的方法
#     result = cv2.matchTemplate(bigPicture_gray, smallPicture_gray, cv2.TM_CCOEFF_NORMED)
#
#     locations = np.where(result >= 0.85)  # 使用np筛选相似度大于等于0.85的
#     locations = list(zip(*locations[::-1]))  # 再次处理仅保留坐标
#
#     if len(locations) > 0:
#       #locations[0][0] 为x轴坐标，locations[0][1] + 140 为y轴坐标脚底
#       print("当前坐标为：", locations[0][0],locations[0][1] + 140)
#
#     cv2.imshow("dnf",ScreenCapture)
#     if cv2.waitKey(5) & 0xFF == ord("q"):
#       cv2.destroyAllWindows()
#       break
#
#
