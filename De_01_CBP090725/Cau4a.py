"""CAU 4a: Khoi tao Tuple va truy cap cac phan tu.
Tuple co thu tu va khong the thay doi sau khi tao.
"""
mon_hoc = ("Python", "C++", "Co so du lieu", "Mang may tinh", "Toan roi rac")
print("Tuple mon hoc:", mon_hoc)

# Chi so (index) bat dau tu 0.
print("Phan tu dau tien:", mon_hoc[0])
print("Phan tu thu hai:", mon_hoc[1])
print("Phan tu thu ba:", mon_hoc[2])

# Chi so am dem tu cuoi ve dau.
print("Phan tu cuoi cung:", mon_hoc[-1])
print("Phan tu ke cuoi:", mon_hoc[-2])

print("\nDanh sach mon hoc:")
for stt, mon in enumerate(mon_hoc, start=1):
    print(f"{stt}. {mon}")

# Tuple tao bang dau ngoac tron (...); index dau tien la 0.
# enumerate() cung cap so thu tu va gia tri khi duyet.
# Co the doc/duyet Tuple nhung khong the gan lai mot phan tu.
