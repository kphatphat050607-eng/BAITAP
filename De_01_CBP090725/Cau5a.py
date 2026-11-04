"""CAU 5a: Dem tan suat xuat hien cua tung ky tu bang Dictionary.
Ket qua co dang {ky_tu: so_lan_xuat_hien}.
"""
def count_freq(s):
    """Nhan chuoi s va tra ve Dictionary thong ke tan suat ky tu."""
    ket_qua = {}

    for ky_tu in s:
        if ky_tu in ket_qua:
            ket_qua[ky_tu] += 1  # Da gap ky tu: tang dem.
        else:
            ket_qua[ky_tu] = 1   # Lan dau gap: bat dau tu 1.

    return ket_qua


chuoi = input("Nhap chuoi can thong ke: ")
tan_suat = count_freq(chuoi)

print("Tan suat xuat hien:")
for ky_tu, so_lan in tan_suat.items():
    print(f"{repr(ky_tu)}: {so_lan}")

# Vi du: 'banana' -> 'b': 1, 'a': 3, 'n': 2.
# Dictionary luu cap key:value; 'in' kiem tra key da ton tai.
# items() duyet ca key va value; return tra ket qua cua ham.
# Ham dem ca khoang trang va phan biet chu hoa/chu thuong.
