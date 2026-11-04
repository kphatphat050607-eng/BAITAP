"""
CAU 3a: Loc cac phan tu co kieu du lieu str trong List.

Danh sach du lieu mau gom nhieu kieu du lieu khac nhau.
isinstance(value, str) giup chi giu lai cac phan tu la chuoi.
"""

ds_ban_dau = [100, "apple", 3.14, "banana", 200, None, "Python", True, ""]

ds_chuoi = []

for phan_tu in ds_ban_dau:
    if isinstance(phan_tu, str):
        ds_chuoi.append(phan_tu)

print("Danh sach ban dau:", ds_ban_dau)
print("Danh sach chi gom chuoi:", ds_chuoi)
print("So phan tu kieu str:", len(ds_chuoi))

"""
Ket qua:
Danh sach chi gom chuoi: ['apple', 'banana', 'Python', '']

Ghi nho:
- List co the chua nhieu kieu du lieu khac nhau.
- isinstance(a, str): kiem tra a co phai chuoi hay khong.
- append(): them phan tu vao cuoi danh sach moi.
- len(): dem so phan tu cua danh sach.
- Dung isinstance thay vi type(...) == str de cach kiem tra linh hoat hon.
"""
