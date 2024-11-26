import time
from pydoc_data.topics import topics

import cv2
import mss
import numpy as np

import Dongeon
import judgeScene
import getObjectLocation
import keyBoard

# defined screen capture area
 # left 表示距离屏幕左边界多少像素
#  top 截图距离上边界多少像素
# width 截图的宽度
# height 截图的高度
CaptureArea = {"left" :0, "top":0, "width" : 800, "height" : 600 }
# monsterIndex=[]
# bossIndex = []
# good_Index = []
# door_Index = []


# //  实例化mss
with mss.mss() as sct:
  while True :
    currentScene = "未知"
    character_Location = (0,0)
    #获取截屏
    ScreenCapture = sct.grab(CaptureArea)
    ScreenCapture = np.array(ScreenCapture)
    # 大部分图片查找时候根据形状和样子来查找，和颜色没有差距。所以转成灰度图片后查找更快
    # opcv 提供将图片转换为灰度的方法
    bigPicture_gray = cv2.cvtColor(ScreenCapture,cv2.COLOR_BGR2GRAY)

    #获取角色坐标代码
    character_Location = getObjectLocation.get_Character_Location(bigPicture_gray)
    print("角色坐标为:",character_Location)

    # 获取场景代码
    currentScene = judgeScene.judgeScene(bigPicture_gray)
    print("当前场景在：", currentScene)
    if currentScene == "赛丽亚":
      time.sleep(1)

    if currentScene == "地下城":
      Dongeon.dongeon(bigPicture_gray,character_Location)

    #获取门坐标并画框
    if len(Dongeon.door_Index) > 0:
      for index in Dongeon.door_Index:
        cv2.rectangle(ScreenCapture, (index[0] - 10, index[1] - 5), (index[0] + 10, index[1]), (255, 255, 255), 2)

      #对怪物进行画框
    if len(Dongeon.monster_Index) > 0:
      for index in Dongeon.monster_Index:
          #rectangle(param1,（param2,param3）,param4,param5)
          #param1 : 图片 param2 画框左上角，param3 画框右下角， param4 RGB颜色 param5边框粗细
        cv2.rectangle(ScreenCapture,(index[0]- 20,index[1] - 20),(index[0] + 20, index[1]+20),(0,0,0),2)

      #获取物品坐标并画框
    if len(Dongeon.good_Index) > 0:
      print("物品坐标：",Dongeon.good_Index)
      for index in Dongeon.good_Index:
        cv2.rectangle(ScreenCapture,(index[0]- 10,index[1] - 5),(index[0] + 10, index[1]),(0,255,255),2)

     #获取boss坐标并画框
    if len(Dongeon.boss_Index) > 0:
      for index in Dongeon.good_Index:
        cv2.rectangle(ScreenCapture, (index[0] - 10, index[1] - 50), (index[0] + 10, index[1]),(0, 0, 255), 2)

    #画出目标方框
    if len(Dongeon.target_Index) > 0:
        cv2.rectangle(ScreenCapture, (Dongeon.target_Index[0] - 20, Dongeon.target_Index[1] - 50), (Dongeon.target_Index[0] + 20, Dongeon.target_Index[1]), (0, 255, 255), 2)

    cv2.imshow("dnf",ScreenCapture)
    if cv2.waitKey(5) & 0xFF == ord("q"):
      cv2.destroyAllWindows()
      keyBoard.releaseAllKey()
      break


