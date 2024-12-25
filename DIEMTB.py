print(F"bang dich vu: \n 1. tinh diem tb. \n 2. muon tim diem cuoi ki de tong tb>8.0. ")
print(F"3. Điểm trung bình của bạn qua từng con điểm cuối kì ")

dv = int(input(f"nhap so dich vu: \n"))

A=str(input(f"nhap 4 con diem mieng(cach nhau bang dau cach): \n"))
B=str(input(f"nhập 2 con điểm ktra giữa và cuối kì(cách nhau bằng dấu cách ):\n"))
C=[float(x) for x in A.split()]
D=[float(x) for x in B.split()]
if dv==1:
  def diem(a,b):
    diem_mieng=sum(a)
    diem_giua_va_cuoi_ki=(b[0]*2)+(b[1]*3)
    print("diem tb: ",(diem_mieng+diem_giua_va_cuoi_ki)/9)
  print(diem(C,D))
if dv==2:
  def diem_2(c,d):
    for i in range(1,10):
      x=i/10.0
      diem_cuoi_ki_1=(sum(c)+d[0]*2+(x*3))/9
      if diem_cuoi_ki_1>8.0:
        print(F"số cần để trên 8.0 là: <{x} ")
        break
  diem_2(C,D)
if dv==3:
  def diem_3(e,f):
    for i in range(1,100):
      x=i/10.0
      diem_cuoi_ki_2=(sum(e)+f[0]*2+(x*3))/9
      print(F"số điểm của bạn =<{x} thì điểm trung bình của bạn là:{diem_cuoi_ki_2} ")
  diem_3(C,D)
