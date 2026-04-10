# Program Operasi Matriks

while True:
    print("\n")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Keluar")

    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 0:
        print("Program selesai.")
        break

    baris = int(input("Input jumlah baris: "))
    kolom = int(input("Input jumlah kolom: "))

    # Matriks pertama
    print("\nMasukkan Matriks Pertama")
    matriks1 = []
    for i in range(baris):
        data = []
        for j in range(kolom):
            nilai = int(input(f"M1[{i}][{j}] = "))
            data.append(nilai)
        matriks1.append(data)

    # Matriks kedua
    print("\nMasukkan Matriks Kedua")
    matriks2 = []
    for i in range(baris):
        data = []
        for j in range(kolom):
            nilai = int(input(f"M2[{i}][{j}] = "))
            data.append(nilai)
        matriks2.append(data)

    hasil = []

    match pilihan:
        case 1:  # Penjumlahan
            for i in range(baris):
                data = []
                for j in range(kolom):
                    data.append(matriks1[i][j] + matriks2[i][j])
                hasil.append(data)

        case 2:  # Pengurangan
            for i in range(baris):
                data = []
                for j in range(kolom):
                    data.append(matriks1[i][j] - matriks2[i][j])
                hasil.append(data)

        case 3:  # Perkalian
            for i in range(baris):
                data = []
                for j in range(kolom):
                    jumlah = 0
                    for k in range(kolom):
                        jumlah += matriks1[i][k] * matriks2[k][j]
                    data.append(jumlah)
                hasil.append(data)

        case _:
            print("Pilihan tidak tersedia")
            continue

    print("\nHasil =")
    for i in range(baris):
        for j in range(kolom):
            print(hasil[i][j], end=" ")
        print()