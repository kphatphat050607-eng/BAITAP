"""
CAU 4a: Khoi tao Tuple va truy cap cac phan tu.
Tuple la tap hop co thu tu va khong the thay doi sau khi tao.
"""

mon_hoc = ("Python", "C++", "Co so du lieu", "Mang may tinh", "Toan roi rac")

print("Tuple mon hoc:", mon_hoc)

# Truy cap bang chi so (index), chi so bat dau tu 0.
print("Phan tu dau tien:", mon_hoc[0])
print("Phan tu thu hai:", mon_hoc[1])
print("Phan tu thu ba:", mon_hoc[2])

# Chi so am dem tu cuoi ve dau.
print("Phan tu cuoi cung:", mon_hoc[-1])
print("Phan tu ke cuoi:", mon_hoc[-2])

# Duyet toan bo Tuple.
print("\nDanh sach mon hoc:")
for i, mon in enumerate(mon_hoc, start=1):
    print(f"{i}. {mon}")

"""
Ghi nho:
- Tuple tao bang dau ngoac tron (...).
- tuple[0] la phan tu dau tien.
- tuple[-1] la phan tu cuoi cung.
- Tuple co the doc va duyet, nhung khong the gan lai phan tu.
- enumerate() tra ve so thu tu va gia tri tung phan tu.
"""
