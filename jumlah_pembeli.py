jumlah_pembeli = int(input("masukan jumlah pembeli tiket: "))
total_harga =0

for i in range(jumlah_pembeli):
    usia = int(input(f"masukan usia pembeli ke-{i+1}: "))
    jumlah_tiket = int(input(f"masukan jumlah tiket yang ingin di beli pembeli ke-{i+1}: "))

    if usia < 12:
        harga_tiket = 30000
    elif usia <= 60:
        harga_tiket = 50000
    else:
        harga_tiket = 35000

    harga_total_per_orang = harga_tiket*jumlah_tiket
    total_harga +=
harga_total_per_orang

    print(f"harga tiket per orang pembeli ke-{i+1}: Rp{harga_total_per_orang:,}")

    print(f"total harga tiket untuk semua pembeli: Rp {total_harga:,}")