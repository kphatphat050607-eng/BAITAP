"""
CAU 5a: Viet ham dem tan suat xuat hien cua tung ky tu trong chuoi.
Ket qua duoc luu trong Dictionary theo dang {ky_tu: so_lan}.
"""

def count_freq(s):
    """
    Tham so:
        s (str): Chuoi can thong ke.
    Tra ve:
        dict: Moi ky tu va so lan xuat hien cua ky tu do.
    """
    ket_qua = {}

    for ky_tu in s:
        if ky_tu in ket_qua:
            # Ky tu da co trong Dictionary: tang so dem them 1.
            ket_qua[ky_tu] += 1
        else:
            # Ky tu xuat hien lan dau: khoi tao gia tri bang 1.
            ket_qua[ky_tu] = 1

    return ket_qua


chuoi = input("Nhap chuoi can thong ke: ")
tan_suat = count_freq(chuoi)

print("Tan suat xuat hien cua cac ky tu:")
for ky_tu, so_lan in tan_suat.items():
    # Dung repr() de nhin ro truong hop ky tu la khoang trang.
    print(f"{repr(ky_tu)}: {so_lan}")

"""
Vi du:
Nhap chuoi: banana
Ket qua:
'b': 1
'a': 3
'n': 2

Ghi nho:
- Dictionary luu du lieu theo cap key:value.
- ky_tu in ket_qua: kiem tra key da ton tai chua.
- += 1: tang bien dem.
- items(): duyet dong thoi key va value.
- Ham return ket_qua de tra Dictionary ve noi goi ham.
- Chuong trinh phan biet chu hoa va chu thuong; khoang trang cung duoc dem.
"""
