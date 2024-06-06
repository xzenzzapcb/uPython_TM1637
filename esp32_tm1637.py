from machine import Pin, I2C
import tm1637
from time import sleep
from ads1x15 import ADS1115

# กำหนดพินสำหรับ TM1637
tm1_clk = Pin(14, Pin.OUT)
tm1_dio = Pin(12, Pin.OUT)

tm2_clk = Pin(27, Pin.OUT)
tm2_dio = Pin(26, Pin.OUT)

tm3_clk = Pin(33, Pin.OUT)
tm3_dio = Pin(25, Pin.OUT)

# สร้างออบเจ็กต์ TM1637 สำหรับแต่ละ 7-segment display
tm1 = tm1637.TM1637(clk=tm1_clk, dio=tm1_dio)
tm2 = tm1637.TM1637(clk=tm2_clk, dio=tm2_dio)
tm3 = tm1637.TM1637(clk=tm3_clk, dio=tm3_dio)

# สร้างออบเจ็กต์ I2C สำหรับการสื่อสารกับ ADS1115
i2c = I2C(scl=Pin(22), sda=Pin(21))  # กำหนดขา SCL และ SDA ที่เหมาะสม

# สร้างออบเจ็กต์ ADS1115
ads = ADS1115(i2c)


# ฟังก์ชันสำหรับแสดงหมายเลขบน 7-segment display
def display_number(tm, number):
    tm.numbers(number // 1000, number % 1000)


# ฟังก์ชันสำหรับอ่านค่าแรงดันจากช่อง ADC
def read_voltage(channel):
    raw = ads.read(channel, gain=1)  # อ่านค่า ADC
    voltage = raw * 4.096 / 32768  # คำนวณแรงดันจากค่า ADC
    return voltage


# ฟังก์ชันสำหรับแปลงแรงดันเป็นกระแส 4-20mA
def voltage_to_current(voltage):
    current = (voltage - 0.5) * (20 - 4) / (3.3 - 0.5) + 4
    return current


try:
    # อ่านค่าแรงดันและแปลงเป็นกระแส จากนั้นแสดงบน 7-segment display แต่ละตัว
    while True:
        voltage1 = read_voltage(0)  # อ่านแรงดันจากช่อง ADC 0
        voltage2 = read_voltage(1)  # อ่านแรงดันจากช่อง ADC 1
        voltage3 = read_voltage(2)  # อ่านแรงดันจากช่อง ADC 2

        current1 = voltage_to_current(voltage1)
        current2 = voltage_to_current(voltage2)
        current3 = voltage_to_current(voltage3)

        # แปลงกระแสเป็นตัวเลขสำหรับแสดงผล
        display_number(tm1, int(current1 * 100))
        display_number(tm2, int(current2 * 100))
        display_number(tm3, int(current3 * 100))

        sleep(1)  # หน่วงเวลา 1 วินาที
except KeyboardInterrupt:
    # เคลียร์หน้าจอเมื่อหยุดโปรแกรม
    tm1.write([0, 0, 0, 0])
    tm2.write([0, 0, 0, 0])
    tm3.write([0, 0, 0, 0])
    print("โปรแกรมหยุดทำงาน")
