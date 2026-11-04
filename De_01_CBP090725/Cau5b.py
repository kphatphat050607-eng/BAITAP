# Cau 5b: Lay ten hoc sinh co diem >= min_score.
def get_high_scores(d, min_score):
    ket_qua = []
    for ten, diem in d.items():
        if diem >= min_score:
            ket_qua.append(ten)
    return ket_qua


score = {"An": 8, "Binh": 6, "Cuong": 9, "Dung": 5, "Hoa": 8}
print(get_high_scores(score, 8))
