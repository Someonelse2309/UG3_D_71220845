awal = int(input("Masukan bilangan awal anda (Dalam Angka)\n>> "))
akhir = int(input("Masukan bilangan akhir anda (Dalam Angka)\n>> "))
barisan = ['']
a = " "
while awal <= akhir:
    None if (awal % 6) == 0 or (awal % 8) == 0 else barisan.append(str(awal))
    awal += 1
print (a.join(barisan))