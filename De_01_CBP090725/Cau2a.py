# Cau 2a: Tinh tong cac so chan trong doan [x, y].
x = int(input("Nhap x: "))
y = int(input("Nhap y: "))

while x > y:
    print("Yeu cau x <= y.")
    x = int(input("Nhap lai x: "))
    y = int(input("Nhap lai y: "))

tong = 0
for i in range(x, y + 1):
    if i % 2 == 0:
        tong += i

print("Tong cac so chan:", tong)
