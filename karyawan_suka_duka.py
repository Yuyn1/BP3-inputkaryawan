print("==input karyawan suka duka==")

nama = input("masukan umur: ")
nik = int(input("masukan nik: "))
status = input("masukan status (pegawai tetap / honor): ")
golongan = input("masukan golongan (A/B/C): ")

if status == "pegawai tetap":
    print("Gaji 1.000.000")
    if golongan == "A":
        print("bonus golongan A +200.000")
        print("total gaji anda 1.200.000")
    elif golongan == "B":
        print("bonus golongan B +400.000")
        print("total gaji anda 1.400.000")
    elif golongan == "C":
        print("bonus golongan C +550.000")
        print("total gaji anda 1.550.000")
if status == "honor":
    print("Gaji 750.000")
    if golongan == "A":
        print("bonus golongan A +150.000")
        print("total gaji anda 900.000")
    elif golongan == "B":
        print("bonus golongan B +275.000")
        print("total gaji anda 1.025.000")
    elif golongan == "C":
        print("bonus golongan C +480.000")
        print("total gaji anda 1.230.000")
else:("input tidak benar")
