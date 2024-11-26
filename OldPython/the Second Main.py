from pydoc_data.topics import topics

import cv2
import mss
import numpy as np

import judgeScene
import getObjectLocation


# defined screen capture area
 # left 表示距离屏幕左边界多少像素
#  top 截图距离上边界多少像素
# width 截图的宽度
# height 截图的高度
CaptureArea = {"left" :0, "top":0, "width" : 800, "height" : 600 }
monsterIndex=[]
bossIndex = []
good_Index = []
door_Index = []





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
    characterLocation = getObjectLocation.get_Character_Location(bigPicture_gray)
    print("角色坐标为:",characterLocation)

    # 获取场景代码
    currentScene = judgeScene.judgeScene(bigPicture_gray)
    print("当前场景在：", currentScene)

    #获取门坐标并画框
    door_Index = getObjectLocation.get_Door_Index(bigPicture_gray)
    print("门坐标为：",door_Index )
    good_Index = getObjectLocation.get_Good_Index(bigPicture_gray)
    if len(door_Index) > 0:
      for index in door_Index:
        cv2.rectangle(ScreenCapture, (index[0] - 10, index[1] - 5), (index[0] + 10, index[1]), (255, 255, 255), 2)



    if currentScene == "地下城":
      monsterIndex = getObjectLocation.get_Monster_Index(bigPicture_gray)
      print("怪物坐标为：", monsterIndex)
      #获取Boss坐标并画框
      bossIndex =  getObjectLocation.get_Boss_Index(bigPicture_gray)
      if len(bossIndex) > 0:
          cv2.rectangle(ScreenCapture, (bossIndex[0] - 10, bossIndex[1] - 50), (bossIndex[0] + 10, bossIndex[1]), (0, 0, 255), 2)

      #对怪物进行画框
      if len(monsterIndex) > 0:
        for index in monsterIndex:
          #rectangle(param1,（param2,param3）,param4,param5)
          #param1 : 图片 param2 画框左上角，param3 画框右下角， param4 RGB颜色 param5边框粗细
          cv2.rectangle(ScreenCapture,(index[0]- 50,index[1] - 50),(index[0] + 50, index[1]+50),(255,255,255),2)

      #获取物品坐标并画框
      good_Index =getObjectLocation.get_Good_Index(bigPicture_gray)
      if len(good_Index) > 0:
        print("物品坐标：",good_Index)
        for index in good_Index:
          cv2.rectangle(ScreenCapture,(index[0]- 10,index[1] - 5),(index[0] + 10, index[1]),(0,255,0),2)


    cv2.imshow("dnf",ScreenCapture)
    if cv2.waitKey(5) & 0xFF == ord("q"):
      cv2.destroyAllWindows()
      break


