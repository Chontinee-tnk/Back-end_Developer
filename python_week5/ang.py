import ex
c=0
d=0
while True:
    q=int(input("เลือกโปรแกรม 1 หรือ 2 :"))
    if q==1:
        print("โปรแกรมเรียงเลข")
        a=int(input('จาก :'))
        b=int(input('ถึง :'))
        print (ex.ex(a,b))
    elif q ==2 :
        y = int(input("ใส่เลข :"))
        c, d = ex.er(y, c, d)
        print((c, d))