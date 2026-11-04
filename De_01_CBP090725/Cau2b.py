"""
CAU 2b: Dem so ky tu chu so trong doan chuoi tu vi tri x den y.

Quy uoc: Vi tri trong de bai tinh tu 1; x va y deu duoc tinh.
Vi du chuoi Python co chi so tu 0 nen can cat s[x - 1:y].
"""

s = input("Nhap chuoi s: ")

# Neu chuoi rong thi khong co vi tri de chon.
if len(s) == 0:
    print("Chuoi rong, khong co ky tu nao de dem.")
else:
    n = len(s)

    def nhap_vi_tri(thong_bao):
        while True:
            try:
                return int(input(thong_bao))
            except ValueError:
                print("Vi tri phai la so nguyen.")

    x = nhap_vi_tri(f"Nhap vi tri x (1..{n}): ")
    y = nhap_vi_tri(f"Nhap vi tri y (1..{n}): ")

    while not (1 <= x <= y <= n):
        print(f"Vi tri khong hop le. Can 1 <= x <= y <= {n}.")
        x = nhap_vi_tri("Nhap lai x: ")
        y = nhap_vi_tri("Nhap lai y: ")

    # Cat chuoi tu vi tri x den y (tinh theo cach dem tu 1).
    doan = s[x - 1:y]
    dem = 0

    for ky_tu in doan:
        if ky_tu.isdigit():
            dem += 1

    print("Doan chuoi duoc chon:", doan)
    print("So ky tu chu so trong doan:", dem)

"""
Vi du:
s = "Python2026"
x = 3, y = 8
Doan chuoi: "thon20"
So ky tu chu so: 2

Ghi nho:
- len(s): lay do dai chuoi.
- s[a:b]: cat chuoi tu chi so a den truoc chi so b.
- isdigit(): True neu ky tu la chu so.
- Vi tri bat dau tu 1 nen chi so Python tuong ung la x - 1.
"""
