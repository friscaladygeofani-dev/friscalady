total_hari = int(input("Masukan Jumlah Hari: "))

tahun = total_hari // 365
sisa_hari = total_hari % 365

bulan = sisa_hari // 30 
hari = sisa_hari % 30

print("\nHasil Konversi:")
print("Bulan :", bulan)
print("Hari :", hari)

