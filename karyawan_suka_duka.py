nama = input("Masukkan Nama : ")
nik = input("Masukkan NIK : ")

status_list = ["Tetap", "Honor"]
golongan_list = ["A", "B", "C"]

gaji = {"Tetap": 1000000, "Honor": 750000}

bonus = {
    "Tetap": {"A": 200000, "B": 400000, "C": 550000},
    "Honor": {"A": 150000, "B": 275000, "C": 480000},
}

total_gaji_tetap = 0
total_gaji_honor = 0

print(f"\nNama: {nama}")
print(f"NIK: {nik}\n")

for status in status_list:
    print(f"Status: {status}")
    for golongan in golongan_list:
        total = gaji[status] + bonus[status][golongan]
        print(f"  Golongan: {golongan}")
        print(f"    Gaji Pokok: {gaji[status]}")
        print(f"    Bonus: {bonus[status][golongan]}")
        print(f"    Total Gaji: {total}\n")
        
        if status == "Tetap":
            total_gaji_tetap += total
        else:
            total_gaji_honor += total

print(f"Total keseluruhan gaji untuk status Tetap: {total_gaji_tetap}")
print(f"Total keseluruhan gaji untuk status Honor: {total_gaji_honor}")