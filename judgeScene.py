import cv2

import numpy as np
#场景列表
scene = ["dixiacheng.png","GameStart.png","sailiya.png","Town.png"]

#定义需要参数大场景灰度图片
def judgeScene(bigPicture_gray):

    # 获取场景代码

    for currentScene in scene:
        # opcv 提供加载图片的方法
        smallPicture = cv2.imread(currentScene)
        smallPicture_gray = cv2.cvtColor(smallPicture, cv2.COLOR_BGR2GRAY)


        # opcv提供在大图片中找小图片的方法
        result = cv2.matchTemplate(bigPicture_gray, smallPicture_gray, cv2.TM_CCOEFF_NORMED)

        locations = np.where(result >= 0.6)  # 使用np筛选相似度大于等于0.85的
        locations = list(zip(*locations[::-1]))  # 再次处理仅保留坐标
        if len(locations) > 0:
            if "GameStart" in currentScene:
                # print("当前在角色选择画面", locations)
                return "角色选择"
            elif "sailiya" in currentScene:
                # time.sleep(3)  # sleep 3s 加延时，延时期间将鼠标点到记事本里，方便调试用
                # res = objdll.M_KeyPress(hdl, 79, 20)  # 打开
                return "赛丽亚"
            elif "Town" in currentScene:
                return "城镇"
            elif "dixiacheng" in currentScene:
                return "地下城"
            break
    return "未知场景"