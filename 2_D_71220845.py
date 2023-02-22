plat = str(input("Masukan Plat Nomor Anda (Pisahkan dengan spasi)\n>> ")).split(" ")
plat1 = plat[1]
try:
    plat1 = (int(plat1))
    if plat1 <= 3000 and plat1 >= 0:
        print ("Plat ini untuk Mobil")
    elif plat1 <= 4000 and plat1 >= 3001 :
        print ("Plat ini untuk Motor")
    elif plat1 <= 5000 and plat1 >= 4001:
        print ("Plat ini untuk Angkutan Umum")
    else:
        print ("Plat ini tidak terindikasi untuk Mobil, Motor atau Angkutan Umum")
except:
    print ("Maaf format anda salah")