"""CAU 1b: Nhap ten, tuoi va in loi chao."""
ten = input("Nhap ho va ten: ").strip()
while ten == "":
    print("Ten khong duoc de trong.")
    ten = input("Nhap lai ho va ten: ").strip()

while True:
    try:
        tuoi = int(input("Nhap tuoi: "))
        if tuoi < 0:
            print("Tuoi khong duoc la so am.")
            continue
        break
    except ValueError:
        print("Tuoi phai la so nguyen. Vui long nhap lai.")

print("\n--- LOI CHAO ---")
print(f"Xin chao {ten}!")
print(f"Ban hien {tuoi} tuoi.")

# input() nhan du lieu dang chuoi; strip() bo khoang trang hai dau.
# int() chuyen tuoi sang so nguyen; try/except xu ly khi nhap sai.
# f-string chen gia tri bien vao chuoi bang {ten}, {tuoi}.
