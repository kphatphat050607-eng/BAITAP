"""
CAU 1b: Nhap ten, tuoi va in loi chao.
"""

ten = input("Nhap ho va ten: ").strip()

# Khong chap nhan ten rong.
while ten == "":
    print("Ten khong duoc de trong.")
    ten = input("Nhap lai ho va ten: ").strip()

# Kiem tra tuoi phai la so nguyen khong am.
while True:
    try:
        tuoi = int(input("Nhap tuoi: "))
        if tuoi < 0:
            print("Tuoi khong duoc la so am.")
            continue
        break
    except ValueError:
        print("Tuoi phai la mot so nguyen. Vui long nhap lai.")

print("\n--- LOI CHAO ---")
print(f"Xin chao {ten}!")
print(f"Ban hien {tuoi} tuoi.")

"""
Vi du:
Nhap ho va ten: Nguyen Van An
Nhap tuoi: 19
Xin chao Nguyen Van An!
Ban hien 19 tuoi.

Ghi nho:
- input(): nhan du lieu dang chuoi.
- strip(): bo khoang trang o dau va cuoi chuoi.
- int(): chuyen chuoi tuoi thanh so nguyen.
- f-string: ghep bien vao chuoi bang cu phap f"...{bien}...".
"""
