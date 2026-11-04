"""CAU 1a: Nhap so thuc va kiem tra chan/le.
Chan/le chi ap dung cho so nguyen. Gia tri 6.0 la so nguyen hop le,
con 6.5 khong the ket luan la chan hay le.
"""
while True:
    try:
        x = float(input("Nhap so thuc x: "))
        break
    except ValueError:
        print("Du lieu khong hop le. Hay nhap mot gia tri so.")

if x.is_integer():
    n = int(x)
    if n % 2 == 0:
        print(f"{n} la so chan.")
    else:
        print(f"{n} la so le.")
else:
    print(f"{x} khong phai so nguyen nen khong xep loai chan/le.")

# Vi du: 12 -> chan; -7 -> le; 6.0 -> chan; 4.5 -> khong xep loai.
# float(): chuyen du lieu sang so thuc; is_integer(): kiem tra phan le;
# int(): ep sang so nguyen; % 2: kiem tra tinh chan/le.
