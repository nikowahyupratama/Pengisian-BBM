
import math
import time

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
    solar = 4500
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
    premium = 5000
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
    pertalite = 7500
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
    pertamax = 10000
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