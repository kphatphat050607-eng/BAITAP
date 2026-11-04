# Cau 5a: Dem tan suat xuat hien cua tung ky tu.
def count_freq(s):
    ket_qua = {}
    for ky_tu in s:
        if ky_tu in ket_qua:
            ket_qua[ky_tu] += 1
        else:
            ket_qua[ky_tu] = 1
    return ket_qua


print(count_freq("hello world"))
