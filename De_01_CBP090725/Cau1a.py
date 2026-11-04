"""
DE SO 01 - CBP090725
CAU 1a: Nhap so thuc x va kiem tra chan/le.

Luu y: So chan va so le la khai niem chi ap dung cho so nguyen.
Neu x la so thuc nhung co phan thap phan bang 0 (vi du 8.0),
ta co the doi sang int de kiem tra. Neu x = 8.5 thi khong ket luan chan/le.
"""

while True:
    try:
        x = float(input("Nhap so thuc x: "))
        break
    except ValueError:
        print("Du lieu khong hop le. Hay nhap mot gia tri so.")

# is_integer() tra ve True neu gia tri float khong co phan le.
if x.is_integer():
    so_nguyen = int(x)

    if so_nguyen % 2 == 0:
        print(f"{so_nguyen} la so chan.")
    else:
        print(f"{so_nguyen} la so le.")
else:
    print(f"{x} khong phai so nguyen nen khong xep loai chan/le.")

"""
Vi du:
- Nhap 12       -> 12 la so chan.
- Nhap -7       -> -7 la so le.
- Nhap 6.0      -> 6 la so chan.
- Nhap 4.5      -> khong xep loai chan/le.

Ghi nho:
- float(input(...)): nhap so thuc.
- is_integer(): kiem tra gia tri float co phan thap phan bang 0.
- int(x): ep kieu sang so nguyen.
- % 2 == 0: so chan; % 2 != 0: so le.
"""
