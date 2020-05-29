
import math
import time

print("-----------------------")
print("    Daftar Karyawan    ")
print("-----------------------")
print("[1] Aby                ")
print("[2] ALifta             ")
print("[3] Banu               ")
print("[4] Niko               ")
print("[5] Surya              ")
print("[6] Yudha              ")

daftar_karyawan = input("Masukkan kode karyawan: ")
dk = daftar_karyawan

while True:
    if dk == "1":
        password = input("Masukkan Password: ")
        if password == "010":
            print("AKSES DISETUJUI")
            break
        else:
            print("AKSES DITOLAK")
    
    elif dk == "2":
        password = input("Masukkan Password: ") 
        if password == "202":
            print("AKSES DISETUJUI")
            break
        else:
            print("AKSES DITOLAK")
    
    elif dk == "3":
        password = input("Masukkan Password: ")
        if password == "330":
            print("AKSES DISETUJUI")
            break
        else:
            print("AKSES DITOLAK")
            
    elif dk == "4":
        password = input("Masukkan Password: ")
        if password == "044":
            print("AKSES DISETUJUI")
            break
        else:
            print("AKSES DITOLAK")
            
    elif dk == "5":
        password = input("Masukkan Password: ")
        if password == "500":
            print("AKSES DISETUJUI")
            break
        else:
            print("AKSES DITOLAK")
            
    elif dk == "6":
        password = input("Masukkan Password: ")
        if password == "006":
            print("AKSES DISETUJUI")
            break
        else:
            print("AKSES DITOLAK")

time = time.ctime()
print ("", time)
print ("==================")
print ("  SELAMAT DATANG  ")
print ("POM BENSIN MANAHAN")
print ("==================")

jenis_BBM=["Solar", "Premium", "Pertalite", "Pertamax"]
metode_Pembelian=["harga", "liter"]

for i in range (4):
    print(i+1, jenis_BBM[i]) 
J = int(input("Jenis BBM: "))

if J == 1:
    solar = 9000
    for i in range (2) :
        print(i+1, metode_Pembelian[i])
    A = int(input("Metode Pembelian :"))
    if A == 1:
        harga = int(input("Nominal pembayaran:"))
        liter = harga/solar
    else :
        liter = int(input("Berapa liter: "))
        harga = liter*solar
    print ("Harga Rp", harga, "sejumlah", liter, "liter")
    
elif J == 2:
    premium = 7000
    for i in range (2) :
        print(i+1, metode_Pembelian[i])
    A = int(input("Metode Pembelian :"))
    if A == 1:
        harga = int(input("Nominal pembayaran:"))
        liter = harga/premium
    else :
        liter = int(input("Berapa liter: "))
        harga = liter*premium
    print ("Harga Rp", harga, "sejumlah", liter, "liter")
    
elif J == 3:
    pertalite = 8000
    for i in range (2) :
        print(i+1, metode_Pembelian[i])
    A = int(input("Metode Pembelian :"))
    if A == 1:
        harga = int(input("Nominal pembayaran:"))
        liter = harga/pertalite
    else :
        liter = int(input("Berapa liter: "))
        harga = liter*pertalite
    print ("Harga Rp", harga, "sejumlah", liter, "liter")
    
else :
    pertamax = 12000
    for i in range (2) :
        print(i+1, metode_Pembelian[i])
    A = int(input("Metode Pembelian :"))
    if A == 1:
        harga = int(input("Nominal pembayaran:"))
        liter = harga/pertamax
    else :
        liter = int(input("Berapa liter: "))
        harga = liter*pertamax
    print ("Harga Rp", harga, "sejumlah", liter, "liter")
    
bayar = int(input("Uang pembayaran: "))
kembalian = bayar-harga
print ("kembalian :", kembalian)

print ("==================================")
print ("  TERIMA KASIH ATAS KEHADIRANNYA  ")
print ("   SEMOGA SELAMAT SAMPAI TUJUAN   ")
print ("==================================")
