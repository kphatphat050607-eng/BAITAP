"""
CAU 2a: Tinh tong cac so chan trong doan [x, y].
Hai dau mut x va y deu duoc tinh trong doan.
"""

def nhap_so_nguyen(thong_bao):
    """Lap lai cho den khi nguoi dung nhap dung so nguyen."""
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("Du lieu khong hop le. Vui long nhap so nguyen.")


x = nhap_so_nguyen("Nhap x: ")
y = nhap_so_nguyen("Nhap y: ")

# Dam bao doan co thu tu tu nho den lon.
while x > y:
    print("Khong hop le: x phai nho hon hoac bang y.")
    x = nhap_so_nguyen("Nhap lai x: ")
    y = nhap_so_nguyen("Nhap lai y: ")

tong = 0
cac_so_chan = []

# y + 1 de range bao gom ca gia tri y.
for i in range(x, y + 1):
    if i % 2 == 0:
        tong += i
        cac_so_chan.append(i)

print("Cac so chan trong doan:", cac_so_chan)
print("Tong cac so chan:", tong)

"""
Vi du:
Nhap x: 1
Nhap y: 8
Cac so chan trong doan: [2, 4, 6, 8]
Tong cac so chan: 20

Ghi nho:
- range(x, y + 1): duyet tu x den y, co tinh y.
- i % 2 == 0: kiem tra i la so chan.
- tong += i: cong don vao bien tong.
- Danh sach rong [] dung de luu cac so chan tim duoc.
"""
