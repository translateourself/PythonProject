import ctypes
import string
import time
from ctypes import *  # 导入 ctypes 库中所有模块
import keyBoard

#定义4个方向变量，记录按键是否按下，避免冲突，加一个前缀x，或y
x_left = 0
x_right = 0
y_up = 0
y_down = 0

#key = 对应技能按键，display_time记录技能释放当时时间，cooling冷却，release_Time释放时间
normal_Skill = [{'key':'q','display_time':0,'cooling_Time':5,'release_Time':0.5},
                {'key':'w','display_time':0,'cooling_Time':3,'release_Time':0.5},
                {'key':'e','display_time':0,'cooling_Time':3,'release_Time':0.5},
                {'key':'r','display_time':0,'cooling_Time':4,'release_Time':0.5}]

ultimate_Skill = [{'key':'j','display_time':0,'cooling_Time':40,'release_Time':0.5}]


#角色移动
def move(character_Index,target_Index):
    global x_left,x_right,y_up,y_down

    #x轴移动逻辑
    if abs(character_Index[0] - target_Index[0]) >= 10:
        if character_Index[0] - target_Index[0] > 0:
            if x_right == 1:
                time.sleep(0.01)
                keyBoard.keyUp('right')
                x_right = 0
            if x_left == 1:
                pass
            elif x_left == 0:
                if abs(character_Index[0] - target_Index[0]) > 80:
                    time.sleep(0.01)
                    keyBoard.keyPress('left')
                    time.sleep(0.05)
                time.sleep(0.01)
                keyBoard.keyDown('left')
                x_left = 1
        elif character_Index[0] - target_Index[0] < 0:
            if x_left == 1:
                time.sleep(0.01)
                keyBoard.keyUp('left')
                x_left = 0
            if x_right == 1:
                pass
            elif x_right == 0:
                if abs(character_Index[0] - target_Index[0]) > 80:
                    time.sleep(0.01)
                    keyBoard.keyPress('right')
                    time.sleep(0.05)
                time.sleep(0.01)
                keyBoard.keyDown('right')
                x_right = 1

        else:
            if x_right == 1:
                time.sleep(0.01)
                keyBoard.keyUp('right')
                x_right = 0
            if x_left == 1:
                time.sleep(0.01)
                keyBoard.keyUp('left')
                x_left = 0

    # y轴移动逻辑
    if abs(character_Index[1] - target_Index[1]) >= 5:
        if character_Index[1] - target_Index[1] > 0:
            if y_down == 1:
                time.sleep(0.01)
                keyBoard.keyUp('down')
                y_down = 0
            if y_up == 1:
                pass
            elif y_up == 0:
                time.sleep(0.01)
                keyBoard.keyDown('up')
                y_up = 1
        elif character_Index[1] - target_Index[1] < 0:
            if y_up == 1:
                time.sleep(0.01)
                keyBoard.keyUp('up')
                y_up = 0
            if y_down == 1:
                pass
            elif y_down == 0:
                time.sleep(0.01)
                keyBoard.keyDown('down')
                y_down = 1
    else:
        if y_up == 1:
            time.sleep(0.01)
            keyBoard.keyUp('up')
            y_up = 0
        if y_down == 1:
            time.sleep(0.01)
            keyBoard.keyUp('down')
            y_down = 0


#停止方法
def stop():
    global x_left,x_right,y_up,y_down
    keyBoard.releaseAllKey()
    if x_left == 1:
        x_left = 0
    if x_right == 1:
        x_right = 0
    if y_down == 1:
        y_down = 0
    if y_up == 1:
        y_up = 0

#攻击普通怪物方法
def attract_Monster(attract_Toward):
    #技能释放次数
    skill_Release_Times = 0
    time.sleep(0.01)
    keyBoard.keyPress(attract_Toward)
    time.sleep(0.01)

    for skill in normal_Skill:
        if(time.time() - skill['display_time']) >= skill['cooling_Time']:
            keyBoard.keyPress(skill['key'])
            time.sleep(0.05)
            skill['display_time'] = time.time()
            skill_Release_Times += 1
            time.sleep(skill['release_Time'])
            #间隔0.5s后释放其他技能
            #time.sleep(0.5)
            #给定技能连续释放次数现在
        if skill_Release_Times >= 1:
            break
    if skill_Release_Times == 0:
        time.sleep(0.01)
        keyBoard.keyPress('x')
        time.sleep(0.01)
        keyBoard.keyPress('x')
        time.sleep(0.01)
        keyBoard.keyPress('x')


#攻击Boss怪物方法
def attract_Boss(attract_Toward):
    #技能释放次数
    skill_Release_Times = 0
    time.sleep(0.01)
    keyBoard.keyPress(attract_Toward)
    time.sleep(0.01)

    for skill in ultimate_Skill:
        if (time.time() - skill['display_time']) > skill['cooling_Time']:
            keyBoard.keyPress(skill['j'])
            time.sleep(0.05)
            skill['display_time'] = time.time()
            time.sleep(skill['release_Time'])

    for skill in normal_Skill:
        if(time.time() - skill['display_time']) > skill['cooling_Time']:
            time.sleep(0.05)
            skill['display_time'] = time.time()
            skill_Release_Times += 1
            time.sleep(skill['release_Time'])
            #间隔0.5s后释放其他技能
            #time.sleep(0.5)
            #给定技能连续释放次数现在
        if skill_Release_Times >= 1:
            break
    if skill_Release_Times == 0:
        time.sleep(0.01)
        keyBoard.keyPress('x')
        time.sleep(0.01)
        keyBoard.keyPress('x')
        time.sleep(0.01)
        keyBoard.keyPress('x')


