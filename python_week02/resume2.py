print("กรุณากรอกข้อมูลส่วนตัว")
name = input("กรุณาป้อนชื่อ :\n")
age =input("โปรดกรอกอายุ :\n")
number=input("โปรดกรอกรหัสประจำตัวนักศึกษา :\n")
stdy =input("โปรดกรอกชั้นปี:\n")
nickname = input("กรุณาป้อนชื่อเล่น :\n")
height =float(input("โปรดกรอกส่วนสูง:\n"))
weight =float(input("โปรดกรอกน้ำหนัก:\n"))
print("ประวัติย่อ")
a = height + weight
print(f"ชื่อ :"+name +"อายุ :"+age +"ปี")
print(f"รหัสประจำตัวนักศึกษา :"+number +"ระดับชั้น:"+stdy)
print("ชื่อเล่น :"+nickname)
print(f"ส่วนสูง :" +str(height) +"เซนติเมตร" + "น้ำหนัก :" +str(weight) +"กิโลกรัม")
print(f"ส่วนสูง + น้ำหนัก =" +str(a))