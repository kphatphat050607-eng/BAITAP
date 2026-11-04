"""CAU 5b: Loc hoc sinh co diem lon hon hoac bang diem chuan.
Dictionary co dang {ten_hoc_sinh: diem}; ham tra ve List ten hoc sinh dat.
"""
def get_high_scores(d, min_score):
    """Tra ve danh sach ten co diem >= min_score."""
    ket_qua = []

    for ten, diem in d.items():
        if diem >= min_score:
            ket_qua.append(ten)

    return ket_qua


scores = {
    "An": 8.0,
    "Binh": 6.5,
    "Cuong": 9.0,
    "Dung": 5.5,
    "Hoa": 8.0,
    "Lan": 7.5
}
diem_chuan = 8.0
ds_dat = get_high_scores(scores, diem_chuan)

print("Bang diem:")
for ten, diem in scores.items():
    print(f"{ten}: {diem}")

print(f"\nHoc sinh co diem >= {diem_chuan}:")
if ds_dat:
    for ten in ds_dat:
        print(f"- {ten}: {scores[ten]}")
else:
    print("Khong co hoc sinh nao dat muc diem yeu cau.")

# Vi du tren: An, Cuong, Hoa dat tu 8 diem tro len.
# items() duyet cap ten-diem; >= tinh ca truong hop bang diem chuan.
# append() them ten vao danh sach; return tra danh sach ket qua.
