
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

time = time.ctime()
def awal () :
    print ("", time)
    print ("==================")
    print (" SELAMAT DATANG DI ")
    print ("   SPBU MANAHAN   ")
    print ("==================")
    print ("     JENIS BBM    ")
    print ("[1] Pertamax      ")
    print ("[2] Pertamax Turbo")
    print ("[3] Pertamina DEX ")
    print ("[4] Premium       ")
    print ("[5] Pertalite     ")
    print ("[6] Dexlite       ")
    print ("[7] Bio Solar     ")
    bbm = input("Masukkan jenis BBM : ")
     if bbm == "1" :
          pertamax()
     elif bbm == "2" :
         pertamaxturbo()
      elif bbm == "3" :
         pertaminadex()
     elif bbm == "4" :
         premium()
     elif bbm == "5" :
         pertalite()
     elif bbm == "6" :
         dexlite()
     elif bbm == "7" :
        biosolar()
     else :
        print ("System Error")
        break
        
metode_Pembelian=["harga", "liter"]

def pertamax():
        Pertamax = 9000
        for i in range (2) :
            print(i+1, metode_Pembelian[i])
        A = int(input("Metode Pembelian : "))
        if A == 1:
            harga = int(input("Nominal pembayaran: "))
            liter = harga/Pertamax
        else :
            liter = int(input("Berapa liter: "))
            harga = liter*Pertamax
        print ("Harga Rp", harga, "sejumlah", liter, "liter")
        bayar = int(input("Uang pembayaran: "))
        kembalian = bayar-harga
        print ("kembalian :", kembalian)
        print ("==================================")
        print ("  TERIMA KASIH ATAS KEHADIRANNYA  ")
        print ("   SEMOGA SELAMAT SAMPAI TUJUAN   ")
        print ("==================================")
    
def pertamaxturbo():
        PertamaxTurbo = 9850
        for i in range (2) :
            print(i+1, metode_Pembelian[i])
        A = int(input("Metode Pembelian :"))
        if A == 1:
            harga = int(input("Nominal pembayaran:"))
            liter = harga/PertamaxTurbo
        else :
            liter = int(input("Berapa liter: "))
            harga = liter*PertamaxTurbo
        print ("Harga Rp", harga, "sejumlah", liter, "liter")
        bayar = int(input("Uang pembayaran: "))
        kembalian = bayar-harga
        print ("kembalian :", kembalian)
        print ("==================================")
        print ("  TERIMA KASIH ATAS KEHADIRANNYA  ")
        print ("   SEMOGA SELAMAT SAMPAI TUJUAN   ")
        print ("==================================")
    
def pertaminadex():
        PertaminaDEX = 10200
        for i in range (2) :
            print(i+1, metode_Pembelian[i])
        A = int(input("Metode Pembelian :"))
        if A == 1:
            harga = int(input("Nominal pembayaran:"))
            liter = harga/PertaminaDEX
        else :
            liter = int(input("Berapa liter: "))
            harga = liter*PertaminaDEX
        print ("Harga Rp", harga, "sejumlah", liter, "liter")
        bayar = int(input("Uang pembayaran: "))
        kembalian = bayar-harga
        print ("kembalian :", kembalian)
        print ("==================================")
        print ("  TERIMA KASIH ATAS KEHADIRANNYA  ")
        print ("   SEMOGA SELAMAT SAMPAI TUJUAN   ")
        print ("==================================")
            
def premium():
        Premium = 6450
        for i in range (2) :
            print(i+1, metode_Pembelian[i])
        A = int(input("Metode Pembelian :"))
        if A == 1:
            harga = int(input("Nominal pembayaran:"))
            liter = harga/Premium
        else :
            liter = int(input("Berapa liter: "))
            harga = liter*Premium
        print ("Harga Rp", harga, "sejumlah", liter, "liter")
        bayar = int(input("Uang pembayaran: "))
        kembalian = bayar-harga
        print ("kembalian :", kembalian)
        print ("==================================")
        print ("  TERIMA KASIH ATAS KEHADIRANNYA  ")
        print ("   SEMOGA SELAMAT SAMPAI TUJUAN   ")
        print ("==================================")
            
def pertalite():
        Pertalite = 7650
        for i in range (2) :
            print(i+1, metode_Pembelian[i])
        A = int(input("Metode Pembelian :"))
        if A == 1:
            harga = int(input("Nominal pembayaran:"))
            liter = harga/Pertalite
        else :
            liter = int(input("Berapa liter: "))
            harga = liter*Pertalite
        print ("Harga Rp", harga, "sejumlah", liter, "liter")
        bayar = int(input("Uang pembayaran: "))
        kembalian = bayar-harga
        print ("kembalian :", kembalian)
        print ("==================================")
        print ("  TERIMA KASIH ATAS KEHADIRANNYA  ")
        print ("   SEMOGA SELAMAT SAMPAI TUJUAN   ")
        print ("==================================")
            
def dexlite():
        Dexlite = 9500
        for i in range (2) :
            print(i+1, metode_Pembelian[i])
        A = int(input("Metode Pembelian :"))
        if A == 1:
            harga = int(input("Nominal pembayaran:"))
            liter = harga/Dexlite
        else :
            liter = int(input("Berapa liter: "))
            harga = liter*Dexlite
        print ("Harga Rp", harga, "sejumlah", liter, "liter")
        bayar = int(input("Uang pembayaran: "))
        kembalian = bayar-harga
        print ("kembalian :", kembalian)
        print ("==================================")
        print ("  TERIMA KASIH ATAS KEHADIRANNYA  ")
        print ("   SEMOGA SELAMAT SAMPAI TUJUAN   ")
        print ("==================================")
    
def biosolar():
        BioSolar = 9400
        for i in range (2) :
            print(i+1, metode_Pembelian[i])
        A = int(input("Metode Pembelian :"))
        if A == 1:
            harga = int(input("Nominal pembayaran:"))
            liter = harga/BioSolar
        else :
            liter = int(input("Berapa liter: "))
            harga = liter*BioSolar
        print ("Harga Rp", harga, "sejumlah", liter, "liter")
        bayar = int(input("Uang pembayaran: "))
        kembalian = bayar-harga
        print ("kembalian :", kembalian)
        print ("==================================")
        print ("  TERIMA KASIH ATAS KEHADIRANNYA  ")
        print ("   SEMOGA SELAMAT SAMPAI TUJUAN   ")
        print ("==================================")


while True:
    if dk == "1":
        password = input("Masukkan Password: ")
        if password == "010":
            print("AKSES DISETUJUI")
            awal ()
        else:
            print("AKSES DITOLAK")
            break
    
    elif dk == "2":
        password = input("Masukkan Password: ") 
        if password == "202":
            print("AKSES DISETUJUI")
            awal ()
        else:
            print("AKSES DITOLAK")
            break
    
    elif dk == "3":
        password = input("Masukkan Password: ")
        if password == "330":
            print("AKSES DISETUJUI")
            awal ()
        else:
            print("AKSES DITOLAK")
            break
            
    elif dk == "4":
        password = input("Masukkan Password: ")
        if password == "044":
            print("AKSES DISETUJUI")
            awal()
        else:
            print("AKSES DITOLAK")
            break
            
    elif dk == "5":
        password = input("Masukkan Password: ")
        if password == "500":
            print("AKSES DISETUJUI")
            awal()
        else:
            print("AKSES DITOLAK")
            break
            
    elif dk == "6":
        password = input("Masukkan Password: ")
        if password == "006":
            print("AKSES DISETUJUI")
            awal ()
        else:
            print("AKSES DITOLAK")
            break
            
