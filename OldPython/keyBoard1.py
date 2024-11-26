
import serial
import time

keyBoardCode = {
    'up' : '32',
    'down' : '51',
    'left' :'50',
    'right' : '4F',
    'w' : '1A',
    'a' :'04',

}

#配置串口参数
ser = serial.Serial('COM9',baudrate=9600,timeout=0.2)

def send(data):
    data_str = ''.join(data)
    hex_data = bytes.fromhex(data_str)
    ser.write(hex_data)
    time.sleep(0.05)
#获取校验码
def verify_sum(dataList):
    total_sum = 0
    for data in dataList:
        total_sum += int(data,16)
        sum = hex(total_sum)[-2:]
    return sum
#实现按下的按键
def pressDown(input):
    dataList = ["57","AB","00","02","08","00","00"]

    dataList.append(keyBoardCode[input])
