import serial
import time

#配置串口参数
ser = serial.Serial('COM9',baudrate=9600,timeout=0.2)

time.sleep(2)

#按下a键
hex_data = bytes.fromhex('57AB000208000004000000000010')
ser.write(hex_data)
time.sleep(1)
#弹起a键

hex_data = bytes.fromhex('57AB000208000004000000000010')
ser.write(hex_data)
time.sleep(0.01)

