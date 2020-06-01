# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:04:17 2020

@author: ASUS
"""

import time

def struk():
    print ("\n")
    print (time)
    print ("==================================")
    print ("        SELAMAT DATANG DI         ")
    print ("           SPBU MANAHAN           ")
    print ("==================================")
    print (time)
    print ("Petugas", "\t :", petugas)
    print ("Pengisian", "\t :", round(liter, 2), "liter")
    print ("Jenis bbm", "\t :" , bbm)
    print ("Total Harga", "\t :", "Rp", harga) 
    bayar = int(input("Pembayaran \t \t : Rp "))
    kembalian = bayar-harga
    print ("Kembali ", "\t : Rp", kembalian)
    print ("==================================")
    print ("  TERIMA KASIH ATAS KEHADIRANNYA  ")
    print ("   SEMOGA SELAMAT SAMPAI TUJUAN   ")
    print ("==================================")
  
def pertamax():
        Pertamax = 9000
        print ("[1] Nominal Rupiah      ")
        print ("[2] Jumlah Liter")
        A = int(input("Metode Pembelian: "))
        global harga
        global liter
        if A == 1:
            harga = int(input("Nominal pembayaran: "))
            liter = harga/Pertamax
            struk()
        elif A == 2:
            liter = int(input("Berapa liter: "))
            harga = liter*Pertamax
            struk()
        else :
            print("Input salah, mohon input ulang!")
            pertamax()
    
def pertamaxturbo():
        PertamaxTurbo = 9850
        print ("[1] Nominal Rupiah      ")
        print ("[2] Jumlah Liter")
        A = int(input("Metode Pembelian: "))
        global harga
        global liter
        if A == 1:
            harga = int(input("Nominal pembayaran: "))
            liter = harga/PertamaxTurbo
            struk()
        elif A == 2:
            liter = int(input("Berapa liter: "))
            harga = liter*PertamaxTurbo
            struk()
        else :
            print("Input salah, mohon input ulang!")
            pertamaxturbo()
    
def pertaminadex():
        PertaminaDEX = 10200
        print ("[1] Nominal Rupiah      ")
        print ("[2] Jumlah Liter")
        A = int(input("Metode Pembelian: "))
        global harga
        global liter
        if A == 1:
            harga = int(input("Nominal pembayaran: "))
            liter = harga/PertaminaDEX
            struk()
        elif A == 2:
            liter = int(input("Berapa liter: "))
            harga = liter*PertaminaDEX
            struk()
        else :
            print("Input salah, mohon input ulang!")
            pertaminadex()
            
def premium():
        Premium = 6450
        print ("[1] Nominal Rupiah      ")
        print ("[2] Jumlah Liter")
        A = int(input("Metode Pembelian: "))
        global harga
        global liter
        if A == 1:
            harga = int(input("Nominal pembayaran: "))
            liter = harga/Premium
            struk()
        elif A == 2:
            liter = int(input("Berapa liter: "))
            harga = liter*Premium
            struk()
        else :
            print("Input salah, mohon input ulang!")
            premium()
            
def pertalite():
        Pertalite = 7650
        print ("[1] Nominal Rupiah      ")
        print ("[2] Jumlah Liter")
        A = int(input("Metode Pembelian: "))
        global harga
        global liter
        if A == 1:
            harga = int(input("Nominal pembayaran: "))
            liter = harga/Pertalite
            struk()
        elif A == 2:
            liter = int(input("Berapa liter: "))
            harga = liter*Pertalite
            struk()
        else :
            print("Input salah, mohon input ulang!")
            pertalite()
            
def dexlite():
        Dexlite = 9500
        print ("[1] Nominal Rupiah      ")
        print ("[2] Jumlah Liter")
        A = int(input("Metode Pembelian: "))
        global harga
        global liter
        if A == 1:
            harga = int(input("Nominal pembayaran: "))
            liter = harga/Dexlite
            struk()
        elif A == 2:
            liter = int(input("Berapa liter: "))
            harga = liter*Dexlite
            struk()
        else :
            print("Input salah, mohon input ulang!")
            dexlite()
    
def biosolar():
        BioSolar = 9400
        print ("[1] Nominal Rupiah      ")
        print ("[2] Jumlah Liter")
        A = int(input("Metode Pembelian: "))
        global harga
        global liter
        if A == 1:
            harga = int(input("Nominal pembayaran: "))
            liter = harga/BioSolar
            struk()
        elif A == 2:
            liter = int(input("Berapa liter: "))
            harga = liter*BioSolar
            struk()
        else :
            print("Input salah, mohon input ulang!")
            biosolar()

print("-----------------------")
print("    Daftar Karyawan    ")
print("-----------------------")
print("[1] Aby                ")
print("[2] Alifta             ")
print("[3] Banu               ")
print("[4] Niko               ")
print("[5] Surya              ")
print("[6] Yudha              ")

daftar_karyawan = input("Masukkan kode karyawan: ")
dk = daftar_karyawan
if dk == "1":
    password = input("Masukkan Password: ")
    if password == "010":
        print("AKSES DISETUJUI")
        print("\n")
        petugas = "Aby"
        login = True
    else:
        print("AKSES DITOLAK")
        login = False
elif dk == "2":
    password = input("Masukkan Password: ") 
    if password == "202":
        print("AKSES DISETUJUI")
        print("\n")
        petugas = "Alifta"
        login = True
    else:
        print("AKSES DITOLAK")
        login = False
elif dk == "3":
    password = input("Masukkan Password: ")
    if password == "330":
        print("AKSES DISETUJUI")
        print("\n")
        petugas = "Banu"
        login = True
    else:
        print("AKSES DITOLAK")
        login = False        
elif dk == "4":
    password = input("Masukkan Password: ")
    if password == "044":
        print("AKSES DISETUJUI")
        print("\n")
        petugas = "Niko"
        login = True
    else:
        print("AKSES DITOLAK")
        login = False     
elif dk == "5":
    password = input("Masukkan Password: ")
    if password == "500":
        print("AKSES DISETUJUI")
        print("\n")
        petugas = "Surya"
        login = True
    else:
        print("AKSES DITOLAK")
        login = False        
elif dk == "6":
    password = input("Masukkan Password: ")
    if password == "006":
        print("AKSES DISETUJUI")
        print("\n")
        petugas = "Yudha"
        login = True
    else:
        print("AKSES DITOLAK")
        login = False
else :
    print("AKSES DITOLAK")

time = time.ctime()

harga = 0
liter = 0   

while login == True:
    print ("=========================")
    print ("    SELAMAT BERTUGAS     ")
    print ("    DI SPBU MANAHAN!     ")
    print ("=========================")
    print ("          MENU           ")
    print ("[1] Pertamax      ")
    print ("[2] Pertamax Turbo")
    print ("[3] Pertamina DEX ")
    print ("[4] Premium       ")
    print ("[5] Pertalite     ")
    print ("[6] Dexlite       ")
    print ("[7] Bio Solar     ")
    print ("[8] Keluar Dari Aplikasi")
    bbm = input("Masukkan Pilihan: ")
    if bbm == "1" :
        bbm = "pertamax"
        pertamax()
    elif bbm == "2" :
        bbm = "pertamaxturbo"
        pertamaxturbo()
    elif bbm == "3" :
        bbm = "pertaminadex"
        pertaminadex()
    elif bbm == "4" :
        bbm = "premium"
        premium()
    elif bbm == "5" :
        bbm = "pertalite"
        pertalite()
    elif bbm == "6" :
        bbm = "dexlite"
        dexlite()
    elif bbm == "7" :
        bbm = "biosolar"
        biosolar()
    elif bbm == "8" :
        break
    else :
        print ("Salah input, mohon input ulang!")
        print ("\n")
        login = True
