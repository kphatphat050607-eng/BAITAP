# Cau 2b: Dem chu so trong cac vi tri x den y (tinh tu 1).
s = input("Nhap chuoi: ")
n = len(s)

x = int(input("Nhap vi tri x: "))
y = int(input("Nhap vi tri y: "))

while not (1 <= x <= y <= n):
    print(f"Vi tri khong hop le. Can 1 <= x <= y <= {n}.")
    x = int(input("Nhap lai x: "))
    y = int(input("Nhap lai y: "))

doan = s[x - 1:y]
dem = 0

for ky_tu in doan:
    if ky_tu.isdigit():
        dem += 1

print("So ky tu chu so:", dem)
