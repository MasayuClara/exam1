jumlah_siswa = int(input("masukan jumlah siswa"))

for i in range(jumlah_siswa+1):
    tugas_1 =float (input("masukan nilai tugas ke 1"))
    tugas_2 =float (input("masukan nilai tugas ke 2"))
    tugas_3 =float (input("masukan nilai tugas ke 3"))

    b=3

    all = tugas_1 + tugas_2 + tugas_3

    avv=all / b

    if avv >= 70:
        print("selamat kamu lulus")

    elif avv >= 50 and avv <= 69:
        print("anda harus perbaiki")

    elif avv < 50:
        print("anda tidak lulus")