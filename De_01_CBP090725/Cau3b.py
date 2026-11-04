"""
CAU 3b: Thuc hanh ba phuong thuc append(), remove(), reverse().
"""

ds = [100, "apple", 3.14, "banana", 200, None]

print("Danh sach ban dau:", ds)

# 1. append(value): them mot phan tu vao cuoi List.
ds.append("orange")
print("Sau append('orange'):", ds)

# 2. remove(value): xoa lan xuat hien dau tien cua gia tri value.
gia_tri_can_xoa = 3.14
if gia_tri_can_xoa in ds:
    ds.remove(gia_tri_can_xoa)
    print(f"Sau remove({gia_tri_can_xoa}):", ds)
else:
    print("Khong tim thay gia tri can xoa.")

# 3. reverse(): dao nguoc thu tu cac phan tu ngay tren List hien tai.
ds.reverse()
print("Sau reverse():", ds)

"""
Ket qua theo danh sach mau:
Ban dau: [100, 'apple', 3.14, 'banana', 200, None]
Sau append: [100, 'apple', 3.14, 'banana', 200, None, 'orange']
Sau remove: [100, 'apple', 'banana', 200, None, 'orange']
Sau reverse: ['orange', None, 200, 'banana', 'apple', 100]

Luu y:
- Cac phuong thuc tren thay doi truc tiep List goc.
- remove() gay loi ValueError neu gia tri khong ton tai, nen kiem tra in truoc.
- reverse() chi dao thu tu, khong sap xep tang/giam.
"""
