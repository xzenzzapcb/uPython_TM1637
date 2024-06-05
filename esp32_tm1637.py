from machine import Pin
import tm1637
from time import sleep

# กำหนดพินสำหรับแต่ละ TM1637
# เลือกพินที่ไม่ใช่ I2C, UART หรือขาอื่นที่ทำให้ ESP32 ทำงานผิดปกติ
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


# ฟังก์ชันสำหรับแสดงหมายเลขบน 7-segment display
def display_number(tm, number):
    tm.numbers(number // 1000, number % 1000)


try:
    # แสดงตัวเลขบน 7-segment display แต่ละตัว
    while True:
        for i in range(10000):
            display_number(tm1, i)
            display_number(tm2, (i + 1234) % 10000)
            display_number(tm3, (i + 5678) % 10000)
            sleep(1)  # หน่วงเวลา 1 วินาที
except KeyboardInterrupt:
    # เคลียร์หน้าจอเมื่อหยุดโปรแกรม
    tm1.write([0, 0, 0, 0])
    tm2.write([0, 0, 0, 0])
    tm3.write([0, 0, 0, 0])
    print("โปรแกรมหยุดทำงาน")
