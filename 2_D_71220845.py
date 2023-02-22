plat = str(input("Masukan Plat Nomor Anda (Pisahkan dengan spasi)\n>> ")).split(" ")
plat1 = plat[1]
try:
    plat1 = (int(plat1))
    if plat1 <= 3000 and plat1 >= 0:
        print ("Plat nomor tersebut diperuntukan untuk Mobil")
    elif plat1 <= 4000 and plat1 >= 3001 :
        print ("Plat nomor tersebut diperuntukan untuk Motor")
    elif plat1 <= 5000 and plat1 >= 4001:
        print ("Plat nomor tersebut diperuntukan untuk Angkutan Umum")
    else:
        print ("Plat nomor tidak terindikasi ketiga angkutan tersebut")
except:
    print ("Plat Nomor Tidak Terinidikasi, harus terdapat nomor kendaraan setelah kode daerah")