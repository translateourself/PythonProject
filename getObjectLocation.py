import os
import threading

import cv2
import mss
import numpy as np


monster_Index = []#定义一个集合，去存多个怪物坐标
good_Index = []
door_Index = []


# 获取角色坐标代码
def get_Character_Location(bigPicture_gray):

    smallPicture = cv2.imread("Character.png")
    smallPicture_gray = cv2.cvtColor(smallPicture, cv2.COLOR_BGR2GRAY)

    # opcv提供在大图片中找小图片的方法
    result = cv2.matchTemplate(bigPicture_gray, smallPicture_gray, cv2.TM_CCOEFF_NORMED)

    locations = np.where(result >= 0.85)  # 使用np筛选相似度大于等于0.85的
    locations = list(zip(*locations[::-1]))  # 再次处理仅保留坐标

    if len(locations) > 0:
        # locations[0][0] 为x轴坐标，locations[0][1] + 140 为y轴坐标脚底
        # print("当前坐标为：", locations[0][0], locations[0][1] + 140)
        return (locations[0][0], locations[0][1] + 140)
    return (0,0)


#在大图片中查找怪物图片
def findPicture(bigPicture_gray,smallPicture_gray,pictureInformation):
    global monster_Index
    result = cv2.matchTemplate(bigPicture_gray,smallPicture_gray,cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.6)  # 使用np筛选相似度大于等于0.85的
    locations = list(zip(*locations[::-1]))  # 再次处理仅保留坐标
    if len(locations) > 0:
        print(locations)
        for location in locations:
            picture_Information = pictureInformation.split("_")
            revise_x = picture_Information[1]
            revise_y = picture_Information[2]
            monster_Index.append((location[0] + int(revise_x),location[1]+ 130 + int(revise_y)))


#获取怪物坐标
def get_Monster_Index(bigPicture_gray):
    global monster_Index
    monster_Index =[]
    tagertMonsterList = os.listdir("Monster/")

#裁剪大图片（130，535）
    bigPicture_gray = bigPicture_gray[130:535,0:799]

    #定义一个线程
    threads = []

    for targetMonsterName in tagertMonsterList:
        smallPicture = cv2.imread("Monster/"+targetMonsterName)
        smallPicture_gray = cv2.cvtColor(smallPicture,cv2.COLOR_BGR2GRAY)

        #创建线程自动开启
        thread = threading.Thread(target = findPicture,args=(bigPicture_gray,smallPicture_gray,targetMonsterName))
        thread.start()
        threads.append(thread)
        #等待多线程处理完成
    for thread in threads:
        thread.join()
    return monster_Index

#获取boss坐标
def get_Boss_Index(bigPicture_gray):
    bigPicture_gray = bigPicture_gray[130:535,0:799]

    smallPicture = cv2.imread("boss.png")
    smallPicture_gray = cv2.cvtColor(smallPicture,cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(bigPicture_gray,smallPicture_gray,cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.85)  # 使用np筛选相似度大于等于0.85的
    locations = list(zip(*locations[::-1]))  # 再次处理仅保留坐标
    if len(locations) >0:
        #+300 表示boss身高
        return [(locations[0][0],locations[0][1] + 130)]
    return []


#在大图片中查找目标物品图片
def find_Good_Picture(bigPicture_gray,smallPicture_gray,good_Name):
    global good_Index
    result = cv2.matchTemplate(bigPicture_gray, smallPicture_gray, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.85)  # 使用np筛选相似度大于等于0.85的
    locations = list(zip(*locations[::-1]))  # 再次处理仅保留坐标
    if len(locations) > 0:
        print(locations)
        for location in locations:
            picture_Information = good_Name.split("_")
            revise_x = picture_Information[1]
            revise_y = picture_Information[2]
            good_Index.append((location[0] + int(revise_x), location[1]+ 130 + int(revise_y)))

#获取物品坐标
def get_Good_Index(bigPicture_gray):
    global  good_Index
    good_Index = []
    good_Index_List = os.listdir("Goods/")
    bigPicture_gray = bigPicture_gray[130:535,0:799]

    # 定义一个线程
    threads = []

    for targetGoodName in good_Index_List:
        smallPicture = cv2.imread("Goods/" + targetGoodName)
        smallPicture_gray = cv2.cvtColor(smallPicture, cv2.COLOR_BGR2GRAY)

        # 创建线程自动开启
        thread = threading.Thread(target=find_Good_Picture, args=(bigPicture_gray, smallPicture_gray, targetGoodName))
        thread.start()
        threads.append(thread)
        # 等待多线程处理完成
    for thread in threads:
        thread.join()
    return good_Index



#在大图片中查找目标门图片
def find_Door_Picture(bigPicture_gray,smallPicture_gray,door_Name):
    global door_Index
    result = cv2.matchTemplate(bigPicture_gray, smallPicture_gray, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.85)  # 使用np筛选相似度大于等于0.85的
    locations = list(zip(*locations[::-1]))  # 再次处理仅保留坐标
    if len(locations) > 0:
        print(locations)
        for location in locations:
            picture_Information = door_Name.split("_")
            revise_x = picture_Information[1]
            revise_y = picture_Information[2]
            door_Index.append((location[0] + int(revise_x), location[1]+ 130 + int(revise_y)))

#获取物品坐标
def get_Door_Index(bigPicture_gray):
    global  door_Index
    door_Index = []
    door_Index_List = os.listdir("Doors/")
    bigPicture_gray = bigPicture_gray[130:535,0:799]

    # 定义一个线程
    threads = []

    for targetDoorName in door_Index_List:
        smallPicture = cv2.imread("Doors/" + targetDoorName)
        smallPicture_gray = cv2.cvtColor(smallPicture, cv2.COLOR_BGR2GRAY)

        # 创建线程自动开启
        thread = threading.Thread(target=find_Door_Picture, args=(bigPicture_gray, smallPicture_gray, targetDoorName))
        thread.start()
        threads.append(thread)
        # 等待多线程处理完成
    for thread in threads:
        thread.join()
    return door_Index



