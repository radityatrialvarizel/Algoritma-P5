# Data mahasiswa
nama = ["Asep", "Budi", "Cecep"]

# Nilai
nilai = [
    [50, 70, 40, 80],
    [78, 78, 80, 65],
    [57, 88, 67, 69]
]

# Cari rata-rata mahasiswa
rata = []

for i in range(len(nilai)):
    r = sum(nilai[i]) / len(nilai[i])
    rata.append(r)

# Cari yang paling tinggi
max_rata = max(rata)
index_max = rata.index(max_rata)

# Cari rata-rata tiap MK
rata_mk = []

for j in range(len(nilai[0])):
    total = 0
    for i in range(len(nilai)):
        total += nilai[i][j]
    rata_mk.append(total / len(nilai))

# Cari yang paling kecil
min_rata = min(rata_mk)
index_min = rata_mk.index(min_rata)

# Output
print("Mahasiswa Terpintar:", nama[index_max], "(Nilai:", round(max_rata,2), ")")
print("Mata Kuliah Nilai Terkecil: MK", index_min+1, "(Nilai:", round(min_rata,2), ")")