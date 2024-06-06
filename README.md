# uPython_TM1637

ก่อนอื่นคุณต้องติดตั้งไลบรารี tm1637 บน MicroPython บน ESP32

1.การติดตั้งไลบรารี tm1637:

1.1.คุณสามารถใช้ Thonny หรือเครื่องมืออื่น ๆ เพื่ออัปโหลดไฟล์tm1637.py ไปยัง ESP32 ของคุณ

1.2.สามารถหาโค้ด tm1637.py ได้จาก ที่นี่ https://github.com/mcauser/micropython-tm1637 ต่อไปนี้เป็นตัวอย่างโค้ด MicroPython

2.เพื่อควบคุม 3 ตัว 4-digit 7-segment display:


![Alt](https://repobeats.axiom.co/api/embed/f0d36e5660126b9dca48f5a745191bbcfd1be3dc.svg "Repobeats analytics image")

เพิ่มการอ่านค่าจาก IC ADS1115 และนำค่า ADC 3 ช่องมาแสดงผลบน 4-digit 7-segment display ทั้ง 3 ตัว

1.ติดตั้งไลบรารี ads1x15:

คุณสามารถใช้ Thonny หรือเครื่องมืออื่น ๆ เพื่ออัปโหลดไฟล์ ads1x15.py ไปยัง ESP32 ของคุณ

2.สามารถหาโค้ด ads1x15.py ได้จาก ที่นี่ https://github.com/robert-hh/ads1x15

ต่อไปนี้เป็นตัวอย่างโค้ด MicroPython เพื่ออ่านค่า ADC 3 ช่องจาก ADS1115 และแสดงผลแรงดันที่ 4-digit 7-segment display ทั้ง 3 ตัว:

อธิบายโค้ด:

1.กำหนดพินสำหรับ TM1637 โดยเลือกพินที่ไม่ใช่ I2C, UART หรือขาอื่นที่อาจทำให้ ESP32 ทำงานผิดปกติ

2.สร้างออบเจ็กต์ TM1637 สำหรับแต่ละ 4-digit 7-segment display

3.สร้างออบเจ็กต์ I2C สำหรับการสื่อสารกับ ADS1115

4.สร้างออบเจ็กต์ ADS1115 เพื่ออ่านค่า ADC

5.ฟังก์ชัน display_number ใช้เพื่อแสดงหมายเลขบน 7-segment display

6.ฟังก์ชัน read_voltage ใช้เพื่ออ่านค่าแรงดันจากช่อง ADC และคำนวณเป็นแรงดันไฟฟ้า

7.ฟังก์ชัน voltage_to_current ใช้เพื่อแปลงแรงดันเป็นค่ากระแส 4-20mA โดยใช้สูตรคำนวณที่กำหนด

8.วนลูปเพื่ออ่านค่าแรงดันจากช่อง ADC ทั้ง 3 ช่อง แปลงเป็นค่ากระแส และแสดงหมายเลขที่คำนวณได้บน 7-segment display แต่ละตัว

9.เมื่อโปรแกรมหยุดทำงาน (โดยการกด Ctrl+C) จะเคลียร์หน้าจอทุก 7-segment display

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=xzenzzapcb/uPython_TM1637&type=Date)](https://star-history.com/#xzenzzapcb/uPython_TM1637&Date)