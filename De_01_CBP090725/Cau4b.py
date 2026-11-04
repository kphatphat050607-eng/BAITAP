"""
CAU 4b: Phep noi Tuple va phep lap Tuple.
"""

t1 = (1, 2)
t2 = (3, 4)

# Phep + noi hai Tuple thanh mot Tuple moi.
tuple_cong = t1 + t2

# Phep * lap lai cac phan tu cua Tuple theo so lan.
tuple_nhan = t1 * 3

print("Tuple t1:", t1)
print("Tuple t2:", t2)
print("t1 + t2 =", tuple_cong)
print("t1 * 3 =", tuple_nhan)

"""
Ket qua:
t1 + t2 = (1, 2, 3, 4)
t1 * 3 = (1, 2, 1, 2, 1, 2)

Luu y:
- + la noi Tuple, khong phai cong tung phan tu.
- * 3 la lap lai Tuple 3 lan.
- Cac phep toan tao Tuple moi, khong lam thay doi t1 va t2.
- Tuple chi co mot phan tu can co dau phay, vi du: (5,).
"""
