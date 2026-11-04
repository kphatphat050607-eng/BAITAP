"""CAU 4b: Phep noi Tuple va phep lap Tuple."""
t1 = (1, 2)
t2 = (3, 4)

# Dau + noi hai Tuple thanh mot Tuple moi.
tuple_cong = t1 + t2

# Dau * lap lai cac phan tu cua Tuple theo so lan.
tuple_nhan = t1 * 3

print("Tuple t1:", t1)
print("Tuple t2:", t2)
print("t1 + t2 =", tuple_cong)
print("t1 * 3 =", tuple_nhan)

# Ket qua:
# t1 + t2 = (1, 2, 3, 4)
# t1 * 3 = (1, 2, 1, 2, 1, 2)
# + la noi Tuple, khong phai cong tung cap phan tu.
# * 3 lap lai Tuple ba lan. Cac phep toan tao Tuple moi.
# Tuple mot phan tu phai co dau phay: (5,).
