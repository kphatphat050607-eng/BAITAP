"""CAU 3b: Thuc hanh append(), remove(), reverse()."""
ds = [100, "apple", 3.14, "banana", 200, None]
print("Danh sach ban dau:", ds)

# 1. append(value): them mot phan tu vao cuoi danh sach.
ds.append("orange")
print("Sau append('orange'):", ds)

# 2. remove(value): xoa lan xuat hien dau tien cua gia tri.
gia_tri_can_xoa = 3.14
if gia_tri_can_xoa in ds:
    ds.remove(gia_tri_can_xoa)
    print(f"Sau remove({gia_tri_can_xoa}):", ds)
else:
    print("Khong tim thay gia tri can xoa.")

# 3. reverse(): dao nguoc thu tu cac phan tu ngay tren danh sach.
ds.reverse()
print("Sau reverse():", ds)

# Luu y: ca ba phuong thuc deu thay doi List tai cho.
# remove() co the gay ValueError neu gia tri khong ton tai,
# do do nen kiem tra bang toan tu in truoc khi xoa.
# reverse() chi dao thu tu, khong sap xep tang dan/giam dan.
