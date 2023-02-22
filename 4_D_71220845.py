nama = (input("Silahkan masukan nama anda\n>> "))
prodi = (input("Silahkan masukan prodi anda\n>> "))
nilai  = (input("Silahkan masukan nilai anda dalam huruf\n>> ")).lower()
try:
    nilai = int(nilai)
    print ("Harap memasukan nilai huruf")
except:
    if nilai == "a":
        print ("Nilai anda 4.00")
    elif nilai == "a-":
        print ("Nilai anda 3.75")
    elif nilai == "b+":
        print ("Nilai anda 3.25")
    elif nilai == "b":
        print ("Nilai anda 3.00")
    elif nilai == "b-":
        print ("Nilai anda 2.75")
    elif nilai == "c+":
        print ("Nilai anda 2.25")
    elif nilai == "c":
        print ("Nilai anda 2.00")
    elif nilai == "d":
        print ("Nilai anda 1.00")
    elif nilai == "e":
        print ("Nilai anda 0.00")
    else:
        print ("Nilai anda tidak terdeteksi")