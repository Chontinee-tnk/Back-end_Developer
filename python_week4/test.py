def choice_area_Rock_Paper_Scissors():
    while True:
        a = int(input("เลือกว่าจะทำอะไร \n เป่ายิงฉุบ คือ 1 \n หาพื้นที่ คือ 2 \n หรือ 0 หยุดการทำงาน \n :"))
        if a == 1:
            print(Rock_Paper_Scissors())
        elif a == 2:
            print(choice_area())
        else :
            break

def Rock_Paper_Scissors():
    import random
    print('โปรแกรมเป่ายิงฉุบ')
    while True:
        a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
        print(a)
        b = str(input("ระบุ :"))
        if b == a :
            print("เสมอ")
        elif a == "กรรไกร" and b == "ค้อน" :
            print("คุณชนะ")
        elif a == "ค้อน" and b == "กระดาษ" :
            print("คุณชนะ")
        elif a == "กระดาษ" and b == "กรรไกร" :
            print("คุณชนะ")
        else:
            print("คุณแพ้")
def choice_area():
    while True:
        a = int(input("เลือกว่าทำอะไร \n สี่เหลี่ยมจัตุรัส คือ 1 \n สี่เหลี่ยมผืนผ้า คือ 2 \n วงกลม คือ 3\n 0 ย้อนกลับ \n :"))
        if a == 1 :
            print(area_square())
        elif a == 2:
            print(area_rectanglr())
        elif a == 3:
            print(area_cirle())
        else:
            print(choice_area_Rock_Paper_Scissors())
def  area_square():
    print("โปรแกรมคำนวณหาพื้นที่ 4 เหลี่ยมจัตุรัส")
    a = int(input('ใส่ด้าน:'))
    sum =a * a
    print(f"ผลลัพธ์ของพื้นที่สี่เหลี่ยมจัตุรัส ={sum}")

def area_rectanglr():
    print("โปรแกรมคำนวณหาพื้นที่สี่เหลี่ยมผืนผ้า")
    c = int(input('ใส่ความกว้าง:'))
    d = int(input('ใส่ความยาว:'))
    sum =c * d
    print(f"ผลลัพธ์ของพื้นที่สี่เหลี่ยมผืนผ้า ={sum}")

def area_cirle():
    print("โปรแกรมคำนวณหาพื้นที่วงกลม")
    t=float(input('รัศมี'))
    f=t*3.14
    print(f"ผลลัพธ์ของพื้นที่วงกลม ={sum}")

print(choice_area_Rock_Paper_Scissors())


