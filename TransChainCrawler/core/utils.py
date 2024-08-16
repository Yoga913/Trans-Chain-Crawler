" program ini digunakan untuk eksplorasi dan analisis jaringan (network analysis),mengurutkan simpul,menampilkan data dalam format tersegmentasi,dan mencari simpul baru yang belum dijelajahi dalam jaringan."

import random

# Fungsi untuk menentukan batasan halaman :yang di perlukan berdasarkan jumplah total `(n)`menggunakan fungsi bulat
def pageLimit(n):
    return int((round(n, 49)/49) + 1)

# Fungsi melakukan Pembulatan angka:Mengatur nilai ke kelipatan tertentu, yang bisa digunakan untuk menyesuaikan atau meratakan jumlah elemen pada suatu batas tertentu.
def round(n, m):
    r = n % m
    return n + m - r if r + r >= m else n - r

# Fungsi untuk mengurutkan data berdasarkan peringkat:digunakan untuk menyusun dan memilih beberapa elemen teratas (top elements) dari sebuah dataset yang mungkin mencerminkan node atau digunakan untuk mengidentifikasi simpul paling berpengaruh dalam jaringan.
def ranker(database, top):
    newDatabase = {}
    for node in database:
        newDatabase[node] = {}
        topSize = [0 for i in range(top)]
        topAdd = ['' for i in range(top)]
        for each in database[node]:
            minimum = min(topSize)
            if database[node][each] > minimum:
                index = topSize.index(minimum)
                topSize[index] = database[node][each]
                topAdd[index] = each
        for size, address in zip(topSize, topAdd):
            newDatabase[node][address] = size
    return newDatabase

# Fungsi untuk melakukan lokasi acak(x,y) :untuk menghasilkan koordinat acak yang digunakan untuk menempatkan node atau elemen lain dalam representasi grafis jaringan, seperti visualisasi peta atau jaringan.
def genLocation():
    x, y = random.randint(1, 800), random.randint(1, 500)
    x, y = random.choice([x, x * -1]), random.choice([y, y * -1])
    return x, y

# Fungsi untuk mendapatkan elemen baru yang belum diproses dari jaringan atau database
def getNew(database, processed):
    new = []
    for address in database:
        if address not in processed:
            new.append(address)
        for childAddress in database[address]:
            if childAddress not in processed:
                new.append(childAddress)
    return set(filter(None, new))

