# DE SO 01 - CBP090725

Bo loi giai Python duoc tach thanh tung y nho. Moi file co the chay doc lap, kem chu thich, du lieu thu va giai thich cu phap quan trong.

## Muc luc bai giai

| Tep | Noi dung |
|---|---|
| `Cau1a.py` | Nhap so thuc va kiem tra chan/le neu gia tri la so nguyen |
| `Cau1b.py` | Nhap ten, tuoi va in loi chao |
| `Cau2a.py` | Tinh tong cac so chan trong doan [x, y] |
| `Cau2b.py` | Dem chu so trong doan chuoi tu vi tri x den y |
| `Cau3a.py` | Loc phan tu kieu `str` trong List |
| `Cau3b.py` | Su dung `append()`, `remove()`, `reverse()` |
| `Cau4a.py` | Khoi tao va truy cap Tuple |
| `Cau4b.py` | Noi va lap Tuple |
| `Cau5a.py` | Dem tan suat ky tu bang Dictionary |
| `Cau5b.py` | Loc hoc sinh theo diem toi thieu |

## Cach chay tren VS Code

1. Cai Python 3 va mo VS Code.
2. Mo thu muc `De_01_CBP090725`.
3. Chon file can chay.
4. Mo Terminal va go lenh:

```bash
python Cau1a.py
python Cau2a.py
python Cau5a.py
```

Neu Windows khong nhan lenh `python`, thu dung:

```bash
py Cau1a.py
```

Moi file doc lap, khong can chay theo thu tu.

## Giai thich tung cau

### Cau 1 - Nhap du lieu va re nhanh

- **1a:** Dung `float(input())` de nhap so thuc. Chan/le chi ap dung cho so nguyen, nen dung `is_integer()` truoc khi ep sang `int`. Sau do `n % 2 == 0` la chan, nguoc lai la le.
- **1b:** Dung `input()` nhap ten, `int()` nhap tuoi. `strip()` loai bo khoang trang thua; vong lap va `try/except` giup yeu cau nhap lai neu ten rong, tuoi am hoac khong phai so nguyen.

### Cau 2 - Vong lap, tong va xu ly chuoi

- **2a:** Duyet tu x den y bang `range(x, y + 1)` de tinh ca hai dau mut. Neu `i % 2 == 0` thi cong i vao tong.
- **2b:** Vi de dem vi tri tu 1 trong khi Python bat dau chi so tu 0, doan x..y duoc cat bang `s[x - 1:y]`. Duyet tung ky tu va dem neu `isdigit()` tra ve True.

### Cau 3 - List

- **3a:** Tao List ket qua rong, duyet List ban dau va dung `isinstance(phan_tu, str)` de chi them phan tu chuoi.
- **3b:** `append(value)` them vao cuoi List; `remove(value)` xoa lan xuat hien dau tien; `reverse()` dao nguoc thu tu hien tai. Ca ba phuong thuc deu thay doi List tai cho.

### Cau 4 - Tuple

- **4a:** Tuple co thu tu. Chi so bat dau tu 0; chi so am dem tu cuoi. Tuple khong cho phep thay doi phan tu sau khi tao.
- **4b:** Phep `+` noi hai Tuple; phep `*` lap lai cac phan tu. Cac phep toan tao Tuple moi va khong sua Tuple ban dau.

### Cau 5 - Dictionary va ham

- **5a:** Dictionary luu moi ky tu lam key va so lan xuat hien lam value. Gap key da co thi tang dem; gap key moi thi gan 1.
- **5b:** Duyet Dictionary bang `items()`; neu diem >= diem chuan thi them ten vao List ket qua. Ham dung `return` de tra danh sach.

## Bang cu phap can nho

| Cu phap | Y nghia |
|---|---|
| `input()` | Nhap du lieu tu ban phim |
| `int()`, `float()` | Chuyen sang so nguyen / so thuc |
| `if / elif / else` | Re nhanh theo dieu kien |
| `while` | Lap khi dieu kien con dung |
| `for`, `range()` | Duyet day gia tri |
| `try / except` | Xu ly loi khi nhap sai kieu |
| `len()` | Lay do dai chuoi/List/Tuple |
| `isdigit()` | Kiem tra ky tu chu so |
| `isinstance(x, str)` | Kiem tra x co phai chuoi |
| `append()` | Them phan tu vao List |
| `remove()` | Xoa gia tri dau tien tim thay |
| `reverse()` | Dao nguoc List tai cho |
| `tuple[index]` | Truy cap phan tu Tuple |
| `dict.items()` | Duyet cap key-value |
| `def`, `return` | Dinh nghia ham va tra ket qua |

## Vi du kiem tra nhanh

| Bai | Du lieu | Ket qua |
|---|---|---|
| 1a | 12; -7; 6.0; 4.5 | Chan; le; chan; khong phai so nguyen |
| 2a | x=1, y=8 | Cac so chan 2,4,6,8; tong 20 |
| 2a | x=3, y=3 | Tong 0 |
| 2b | s=Python2026, x=3, y=8 | Doan thon20; dem 2 chu so |
| 5a | banana | b:1, a:3, n:2 |
| 5b | Diem chuan 8 | An, Cuong, Hoa |

## Cac quy uoc va luu y

1. **Cau 1a:** Neu de ghi "so thuc" va yeu cau chan/le, can xu ly ro so thuc khong nguyen. Chan/le chi co nghia voi so nguyen; 6.0 co the xem la 6, con 6.5 khong phai so nguyen.
2. **Cau 2b:** Bai giai hieu x va y la vi tri dem tu 1, tinh ca hai dau mut. Neu ban goc cua de quy dinh khac, can doi phep cat chuoi tuong ung.
3. **Cau 3a, 3b va Cau 4:** Cac tep dung du lieu mau de minh hoa thao tac. Neu de thi cung cap List/Tuple cu the, thay du lieu mau bang du lieu cua de.
4. **Cau 5a:** Ham dem tat ca ky tu, bao gom khoang trang; chu hoa va chu thuong duoc tinh rieng.
5. Cac vi du va du lieu mau co the thay doi, nhung cach xu ly chinh van giu nguyen.

## Checklist tu on tap

- [ ] Tu nhap va kiem tra du lieu.
- [ ] Tu viet vong lap tinh tong va dem.
- [ ] Tu cat chuoi va kiem tra ky tu.
- [ ] Tu loc phan tu trong List.
- [ ] Tu truy cap, noi va lap Tuple.
- [ ] Tu viet ham thao tac voi Dictionary.
