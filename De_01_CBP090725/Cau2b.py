"""CAU 2b: Dem chu so trong doan chuoi tu vi tri x den y.
Quy uoc x, y dem tu 1 va tinh ca hai dau mut.
"""
s = input("Nhap chuoi s: ")
n = len(s)

if n == 0:
    print("Chuoi rong, khong co ky tu de dem.")
else:
    def nhap_vi_tri(thong_bao):
        while True:
            try:
                return int(input(thong_bao))
            except ValueError:
                print("Vi tri phai la so nguyen.")

    x = nhap_vi_tri(f"Nhap vi tri x (1..{n}): ")
    y = nhap_vi_tri(f"Nhap vi tri y (1..{n}): ")
    while not (1 <= x <= y <= n):
        print(f"Can thoa man 1 <= x <= y <= {n}.")
        x = nhap_vi_tri("Nhap lai x: ")
        y = nhap_vi_tri("Nhap lai y: ")

    doan = s[x - 1:y]  # Vi tri de bai tu 1, chi so Python tu 0.
    dem = 0
    for ky_tu in doan:
        if ky_tu.isdigit():
            dem += 1

    print("Doan chuoi duoc chon:", doan)
    print("So ky tu chu so:", dem)

# Vi du: s='Python2026', x=3, y=8 -> doan='thon20', co 2 chu so.
# len() lay do dai; s[a:b] cat chuoi; isdigit() kiem tra chu so.
