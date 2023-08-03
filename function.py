# สร้างฟังก์ชันแบบไม่มีการรับค่า และไม่มีการส่งค่ากลับ
def hello():
    print("Hello World")


# เรียกใช้งานฟังก์ชัน hello()
hello()


# สร้างฟังก์ชันแบบมีการรับค่า และไม่มีการส่งค่ากลับ
def info(msg):
    print("Welcome", msg)


# เรียกใช้งานฟังก์ชัน info()
info("Python")


# สร้างฟังก์ชันแบบไม่มีการรับค่า และมีการส่งค่ากลับ
def area(width=0, height=0, *args):
    return width * height


# เรียกใช้งานฟังก์ชัน area()
print("Area =", area())
print("Area =", area(20))
print("Area =", area(20, 30, 40, 50))
