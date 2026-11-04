"""CAU 2a: Tinh tong cac so chan trong doan [x, y] (tinh ca hai dau mut)."""
def nhap_so_nguyen(thong_bao):
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("Du lieu khong hop le. Vui long nhap so nguyen.")

x = nhap_so_nguyen("Nhap x: ")
y = nhap_so_nguyen("Nhap y: ")
while x > y:
    print("Khong hop le: x phai nho hon hoac bang y.")
    x = nhap_so_nguyen("Nhap lai x: ")
    y = nhap_so_nguyen("Nhap lai y: ")

tong = 0
cac_so_chan = []
for i in range(x, y + 1):
    if i % 2 == 0:
        cac_so_chan.append(i)
        tong += i

print("Cac so chan trong doan:", cac_so_chan)
print("Tong cac so chan:", tong)

# Vi du x=1, y=8 -> cac so chan [2, 4, 6, 8], tong = 20.
# range(x, y+1) bao gom ca y; % 2 == 0 nhan dien so chan;
# tong += i la cong don. Neu khong co so chan, tong van bang 0.
