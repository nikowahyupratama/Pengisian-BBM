import time
import pandas as pd

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
    print ('\n')
    lp = {}
    lp['Petugas'] = petugas
    lp['BBM'] = bbm
    lp['Harga/L'] = nominal
    lp['Total Keluar(L)'] = round(liter, 2)
    lp['Total Transaksi'] = harga
    laporan.append(lp)
    
def transaksi():
    df = pd.read_csv("bbm.csv")
    print ("[1] Nominal Rupiah      ")
    print ("[2] Jumlah Liter")
    A = int(input("Metode Pembelian: "))
    global nominal
    nominal = df["Harga"][row]
    global harga
    global liter
    if A == 1:
        harga = int(input("Nominal pembayaran: "))
        liter = harga/nominal
        struk()
    elif A == 2:
        liter = int(input("Berapa liter: "))
        harga = liter*nominal
        struk()
    else :
        print("Input salah, mohon input ulang!")
        transaksi()
        
def report():
    ini = pd.DataFrame(laporan)
    ini = ini[['Petugas', 'BBM', 'Harga/L',
               'Total Keluar(L)', 'Total Transaksi']]
    print('\n')
    print('LAPORAN TRANSAKSI')
    print("=================")
    print(ini)
    final = ini[['Total Keluar(L)', 'Total Transaksi']]
    ffinal = final.sum(axis = 0)
    print('\n')
    print('TOTAL KESELURUHAN TRANSAKSI')
    print("===========================")
    print(ffinal)
    
def updateharga() :
    print ("==================================")
    print ("         UPDATE HARGA BBM         ")
    print ("==================================")
    print ("[1] Pertamax      ")
    print ("[2] Pertamax Turbo")
    print ("[3] Pertamina DEX ")
    print ("[4] Premium       ")
    print ("[5] Pertalite     ")
    print ("[6] Dexlite       ")
    print ("[7] Bio Solar     ")
    bbm = input("Masukkan Pilihan: ")
    hbaru = input("Masukkan Harga Baru: ")
    if bbm == "1" :
        bbm = "Pertamax"
        row = 0
    elif bbm == "2" :
        bbm = "Pertamax Turbo"
        row = 1
    elif bbm == "3" :
        bbm = "Pertamina Dex"
        row = 2
    elif bbm == "4" :
        bbm = "Premium"
        row = 3
    elif bbm == "5" :
        bbm = "Pertalite"
        row = 4
    elif bbm == "6" :
        bbm = "Dexlite"
        row = 5
    elif bbm == "7" :
        bbm = "Bio Solar"
        row = 6
    
    df = pd.read_csv("bbm.csv")
    
    df.at[row] = bbm , hbaru
    df.to_csv("bbm.csv", index=False)
    print('\n')
    print("DAFTAR HARGA BBM TERBARU")
    print("========================")
    print(df)
    global login
    login = True

  
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
row = 0
laporan = []

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
    print ("[8] Update Harga")
    print ("[9] Keluar Aplikasi (Belum ada Transaksi)")
    print ("[0] Keluar Aplikasi (Sudah ada transaksi)")
    print ("PERINGATAN: bila memilih [0] tetapi belum ada transaksi, maka akan terjadi error")
    global bbm
    bbm = input("Masukkan Pilihan: ")
    if bbm == "1" :
        bbm = "Pertamax"
        row = 0
        transaksi()
    elif bbm == "2" :
        bbm = "Pertamax Turbo"
        row = 1
        transaksi()
    elif bbm == "3" :
        bbm = "Pertamina Dex"
        row = 2
        transaksi()
    elif bbm == "4" :
        bbm = "Premium"
        row = 3
        transaksi()
    elif bbm == "5" :
        bbm = "Pertalite"
        row = 4
        transaksi()
    elif bbm == "6" :
        bbm = "Dexlite"
        row = 5
        transaksi()
    elif bbm == "7" :
        bbm = "Bio Solar"
        row = 6
        transaksi()
    elif bbm == "8" :
        updateharga()
    elif bbm == "9" :
        break
    elif bbm == "0" :
        report()
        break
    else :
        print ("Salah input, mohon input ulang!")
        login = True
