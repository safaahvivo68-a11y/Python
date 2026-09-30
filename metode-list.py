nilai    = [85, 92, 78, 95, 70]
buah     = ['apel', 'manggga', 'pisang' ]
campuran = [1, 'phyton', 3.14, True]

print(nilai [0])    # 85    (indeks pertama = 0)
print(nilai [-1])   # 70    (indeks negatif = dari brlakang)
print(buah [1])     # 'mangga'

print(nilai[1:4])   # [92, 78, 95]  (indeks 1 s.d. 3)
print(nilai[:3])    # [85, 92, 78]  (dari awal s.d. indeks 2)           
print(nilai[2:])    # [78, 95, 70]  (dari indeks 2 s.d. akhir)               
print(nilai[::2])   # [85, 78, 70]  (setiap 2 langkah)