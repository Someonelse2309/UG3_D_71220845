nama = (input("Silahkan masukan nama anda\n>> "))
prodi = (input("Silahkan masukan prodi anda\n>> "))
nilai  = (input("Silahkan masukan nilai anda dalam huruf\n>> ")).lower()
try:
    nilai = int(nilai)
    print ("Harap memasukan nilai huruf")
except:
    if nilai == "a":
        print ("Nilai anda adalah 4.00, tbl tbl serem bgt loh")
    elif nilai == "a-":
        print ("Nilai anda adalah 3.75, kamu keren!!")
    elif nilai == "b+":
        print ("Nilai anda adalah 3.25, tapi sayangnya ga 4.00 ga skuy")
    elif nilai == "b":
        print ("Nilai anda adalah 3.00, cupu ga 4.00")
    elif nilai == "b-":
        print ("Nilai anda adalah 2.75, kurang semangat belajar nihh")
    elif nilai == "c+":
        print ("Nilai anda adalah 2.25, magang aja 3 bulan masa lu cuma 2,25")
    elif nilai == "c":
        print ("Nilai anda adalah 2.00, cupu lu")
    elif nilai == "d":
        print ("Nilai anda adalah 1.00 apakah sudah anda pikirkan untuk pindah jurusan?")
    elif nilai == "e":
        print ("Nilai anda adalah 0.00, niat kuliah nggak sih???")
    else:
        print ("Nilai anda masukan tidak valid")