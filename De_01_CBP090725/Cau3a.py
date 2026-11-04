# Cau 3a: Tao danh sach moi chi gom cac phan tu kieu str.
lst = [100, "apple", 3.14, "banana", 200, None]

ds_chuoi = []
for phan_tu in lst:
    if isinstance(phan_tu, str):
        ds_chuoi.append(phan_tu)

print("Danh sach chuoi:", ds_chuoi)
