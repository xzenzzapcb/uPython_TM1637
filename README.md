# uPython_TM1637

ก่อนอื่นคุณต้องติดตั้งไลบรารี tm1637 บน MicroPython บน ESP32

1.การติดตั้งไลบรารี tm1637:

1.1.คุณสามารถใช้ Thonny หรือเครื่องมืออื่น ๆ เพื่ออัปโหลดไฟล์tm1637.py ไปยัง ESP32 ของคุณ

1.2.สามารถหาโค้ด tm1637.py ได้จาก ที่นี่ https://github.com/mcauser/micropython-tm1637 ต่อไปนี้เป็นตัวอย่างโค้ด MicroPython

2.เพื่อควบคุม 3 ตัว 4-digit 7-segment display:

อธิบายโค้ด:

1.กำหนดพินสำหรับแต่ละ TM1637 โดยเลือกพินที่ไม่ใช่ I2C, UART หรือขาอื่นที่อาจทำให้ ESP32 ทำงานผิดปกติ

2.สร้างออบเจ็กต์ TM1637 สำหรับแต่ละ 4-digit 7-segment display

ฟังก์ชัน display_number ใช้เพื่อแสดงหมายเลขบน 7-segment display

3.วนลูปเพื่อแสดงหมายเลขเพิ่มขึ้นทีละหนึ่งทุก ๆ 1 วินาทีบนแต่ละ 7-segment display

4.เมื่อโปรแกรมหยุดทำงาน (โดยการกด Ctrl+C) จะเคลียร์หน้าจอทุก 7-segment display

หวังว่าจะเป็นประโยชน์สำหรับโปรเจ็คของคุณครับ! หากมีคำถามเพิ่มเติมหรือต้องการคำแนะนำเพิ่มเติม บอกได้เลยครับ!

![Alt](https://repobeats.axiom.co/api/embed/f0d36e5660126b9dca48f5a745191bbcfd1be3dc.svg "Repobeats analytics image")

เพิ่มการอ่านค่าจาก IC ADS1115 และนำค่า ADC 3 ช่องมาแสดงผลบน 4-digit 7-segment display ทั้ง 3 ตัว

1.ติดตั้งไลบรารี ads1x15:

คุณสามารถใช้ Thonny หรือเครื่องมืออื่น ๆ เพื่ออัปโหลดไฟล์ ads1x15.py ไปยัง ESP32 ของคุณ

2.สามารถหาโค้ด ads1x15.py ได้จาก ที่นี่ https://github.com/robert-hh/ads1x15

ต่อไปนี้เป็นตัวอย่างโค้ด MicroPython เพื่ออ่านค่า ADC 3 ช่องจาก ADS1115 และแสดงผลแรงดันที่ 4-digit 7-segment display ทั้ง 3 ตัว:
