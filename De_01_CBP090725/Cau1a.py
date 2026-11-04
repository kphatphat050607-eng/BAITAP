# De so 01 - CBP090725
# Cau 1a: Nhap so thuc x va kiem tra chan/le.
# Luu y: Khai niem chan/le chi ap dung cho so nguyen.
x = float(input("Nhap x: "))

if x.is_integer():
    if int(x) % 2 == 0:
        print("Chan")
    else:
        print("Le")
else:
    print("x khong phai so nguyen nen khong the ket luan chan/le.")
