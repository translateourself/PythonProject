import getObjectLocation
import character_Action

monster_Index =[]
boss_Index = []
good_Index = []
door_Index = []

targetType =''
target_Index =()

def dongeon(bigPicture_gray,character_Index):
    #初始化变量
    global monster_Index,boss_Index,good_Index,door_Index
    global targetType,target_Index

    monster_Index = []
    boss_Index = []
    good_Index = []
    door_Index = []
    targetType = ''
    target_Index = ()

    monster_Index = getObjectLocation.get_Monster_Index(bigPicture_gray)

    boss_Index = getObjectLocation.get_Boss_Index(bigPicture_gray)

    good_Index = getObjectLocation.get_Good_Index(bigPicture_gray)

    door_Index = getObjectLocation.get_Door_Index(bigPicture_gray)

    #目标选择策略
    #如果有boss那么目标为BOSS
    if len(boss_Index) > 0:
        targetType = 'boss'
        target_Index = boss_Index[0]
    #如果有怪物没有物品
    elif len(monster_Index) > 0 and len(good_Index) == 0:
        targetType = 'monster'
        target_Index = shortest_Index(monster_Index,character_Index)
        #如过又有目标，又有怪，则选当怪与角色距离> 物品与角色距离+ 150 时候优先拿物品
    elif len(monster_Index) > 0 and len(good_Index) > 0:
        shortest_Monster = shortest_Index(monster_Index,character_Index)
        shortest_Good = shortest_Index(good_Index,character_Index)
        #计算最近怪物,物品坐标和角色坐标的距离
        monster_Character_Distance = abs(character_Index[0] - shortest_Monster[0]) +abs(character_Index[1] - shortest_Monster[1])
        good_Character_Distance = abs(character_Index[0] - shortest_Good[0]) +abs(character_Index[1] - shortest_Good[1])

        if good_Character_Distance < monster_Character_Distance and abs(good_Character_Distance - monster_Character_Distance) >150:
            targetType = 'good'
            target_Index = shortest_Good
        else:
            targetType = 'monster'
            target_Index = shortest_Monster
    elif len(monster_Index) == 0 and len(good_Index) > 0:
        targetType = 'good'
        target_Index = shortest_Index(good_Index,character_Index)
    elif len(door_Index) > 0:
        targetType = 'door'
    else:
        targetType = ''
        target_Index = []
    print('当前目标为：',target_Index)

    # 根据目标进行动作
    if targetType == 'boss':
        #先进行boss范围判定
        if abs(character_Index[1] - target_Index[1] <= 20) and abs(character_Index[0] - target_Index[0]) <= 200:
            action = 'attract boss'
            print("攻击Boss")
            character_Action.stop()
            if character_Index[0] - target_Index[0] > 0:
                #攻击boss
                character_Action.attract_Boss('left')
                pass
            else:
                character_Action.attract_Boss('right')
                pass
        else:
            action = 'move to Boss'
            print('移动到Boss附近')
            character_Action.move(character_Index,target_Index)
    #如果目标是怪物
    elif targetType == 'monster':
        if abs(character_Index[1] - target_Index[1] ) <= 20 and abs(character_Index[0] - target_Index[0]) <= 200:
            action = 'attract monster'
            print('攻击monster')
            character_Action.stop()
            if character_Index[0] - target_Index[0] > 0:
                character_Action.attract_Monster('left')
                pass
            else:
                character_Action.attract_Monster('right')
                pass
        else:
            action = 'move to monster'
            print('移动到monster附近')
            character_Action.move(character_Index, target_Index)
    #目标是物品
    elif  targetType == 'good':
        if abs(character_Index[1] - target_Index[1] <= 5) and abs(character_Index[0] - target_Index[0]) <= 10:
            action = 'pick up good'
            print('捡东西')
            #自动捡物品
            character_Action.stop()
        else:
            print('移动到物品上')
            action = '移动到物品上'
            character_Action.move(character_Index, target_Index)
    #目标是门
    elif  targetType == 'door':
        if abs(character_Index[1] - target_Index[1] <= 10) and abs(character_Index[0] - target_Index[0]) <= 10:
            action = 'enter the door'
            print('进门')
            #自动捡物品
            character_Action.stop()
        else:
            print('移动到门里')
            action = '移动到门里'
            character_Action.move(character_Index, target_Index)
    #目标是空
    elif  targetType == '':
        character_Action.stop()







#最近目标
def shortest_Index(coordinates_List,given_coordinate):
    min_distance = None
    shortest_Index = None

    #计算曼哈顿距离并找到最近坐标
    for coord in coordinates_List:
        x1, y1 = given_coordinate
        x2, y2 = coord
        distance = abs(x1 - x2) + abs(y1 - y2)

        #如果第一个坐标或者距离更近，则更新最小距离已经最近目标
        if min_distance is None or distance < min_distance:
            min_distance = distance
            shortest_Index = coord
    return shortest_Index

