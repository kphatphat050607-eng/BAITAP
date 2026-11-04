"""CAU 3a: Loc cac phan tu co kieu str trong List."""
ds_ban_dau = [100, "apple", 3.14, "banana", 200, None, "Python", True, ""]

ds_chuoi = []
for phan_tu in ds_ban_dau:
    if isinstance(phan_tu, str):
        ds_chuoi.append(phan_tu)

print("Danh sach ban dau:", ds_ban_dau)
print("Danh sach chi gom chuoi:", ds_chuoi)
print("So phan tu kieu str:", len(ds_chuoi))

# isinstance(value, str) kiem tra phan tu co phai chuoi hay khong.
# append() them phan tu vao cuoi List moi; len() dem so phan tu.
# List moi khong lam thay doi List ban dau.
