import random

#Daftar ini memberikan gambaran tentang waktu acara.
Kalimat_starter = random.randint(1, 3)
if Kalimat_starter == 1 :
    kalimat_1 = ("Pada hari senin, ")
if Kalimat_starter == 2 :
    kalimat_1 = ("Pada hari selasa, ")
if Kalimat_starter == 3 :
    kalimat_1 = ("Pada hari rabu, ")

#Daftar ini menceritakan tentang karakter utama dari cerita ini.
karakter = random.randint(1, 3)
if karakter == 1 :
    kalimat_2 = ("Mingyu sedang mengerjakan tugas ")
if karakter == 2 :
    kalimat_2 = ("Mingyu sedang membaca ")
if karakter == 3 :
    kalimat_2 = ("Mingyu sedang menulis ")

#Daftar ini menentukan hari yang tepat di mana beberapa insiden telah terjadi.
waktu = random.randint(1, 3)
if waktu == 1 :
    kalimat_3 = ("dan pada hari senin ini ia sedang sibuk")
if waktu == 2 :
    kalimat_3 = ("dan pada hari selasa ini ia sedang rajin ")
if waktu == 3 :
    kalimat_3 = ("dan pada hari rabu ini ia sedang bersemangat ")

#Daftar ini mendefinisikan plot cerita.
story_plot = random.randint(1, 3)
if story_plot == 1 :
    kalimat_4 = ("karena hari sibuk, ")
if story_plot == 2 :
    kalimat_4 = ("karena ia sedang tidak sibuk, ")
if story_plot == 3 :
    kalimat_4 = ("karena banyak hal yang perlu dialakukan, ")

#Daftar ini mendefinisikan tempat di mana insiden itu terjadi.
tempat = random.randint(1, 3)
if tempat == 1 :
    kalimat_5 = ("ia mengerjakanya di taman, ")
if tempat == 2 :
    kalimat_5 = ("ia mengerjakan di cafe, ")
if tempat == 3 :
    kalimat_5 = ("ia mengerjakan di kamar, ")

#Daftar ini mendefinisikan karakter kedua dari cerita.
second_character = random.randint(1, 3)
if second_character == 1 :
    kalimat_6 = ("sedangkan ayah mencuci mobil ")
if second_character == 2 :
    kalimat_6 = ("sedangkan ibu sedang memasak ")
if second_character == 3 :
    kalimat_6 = ("sedangkan adik sedang menari ")

#Daftar ini mendefinisikan usia karakter kedua.
usia = random.randint(1, 3)
if usia == 1 :
    kalimat_7 = ("karena usianya sudah 45 tahun ")
if usia == 2 :
    kalimat_7 = ("karena usianya sudah 42 tahun ")
if usia == 3 :
    kalimat_7 = ("karena usianya sudah 14 tahun ")

#Daftar ini menceritakan tentang pekerjaan yang dilakukan karakter kedua.
pekerjaan = random.randint(1, 3)
if pekerjaan == 1 :
    kalimat_8 = ("karena ia sedang tidak bekerja.")
if pekerjaan == 2 :
    kalimat_8 = ("karenanya ia sedang menghabiskan waktu luang ")
if pekerjaan == 3 :
    kalimat_8 = ("karenanya ia tidak memiliki kegiatan yang penting")

print (kalimat_1, kalimat_2, kalimat_3, kalimat_4, kalimat_5, kalimat_6, kalimat_7, kalimat_8)