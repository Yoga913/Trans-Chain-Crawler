#!/usr/bin/env python3

import os
import json
import random
import argparse
import webbrowser
import concurrent.futures

from time import sleep

from core.utils import getNew
from core.utils import ranker
from core.utils import genLocation
from core.getQuark import getQuark
from core.exporter import exporter
from core.prepareGraph import prepareGraph
from core.getTransactions import getTransactions
from core.colors import green, white, red, info, run, end

# Inisialisasi parser argumen untuk mengambil input dari pengguna
parser = argparse.ArgumentParser(description='Sebuah program untuk merayapi alamat blockchain.')

# Menambahkan opsi untuk memasukkan alamat blockchain target
parser.add_argument('-s', '--seeds', help='alamat blockchain target', dest='seeds')
# Menambahkan opsi untuk memasukkan file output untuk menyimpan data JSON mentah
parser.add_argument('-o', '--output', help='file output untuk menyimpan data JSON mentah', dest='output')
# Menambahkan opsi untuk menentukan kedalaman perayapan
parser.add_argument('-d', '--depth', help='kedalaman perayapan', dest='depth', type=int, default=3)
# Menambahkan opsi untuk menentukan jumlah alamat yang akan dirayapi dari hasil
parser.add_argument('-t', '--top', help='jumlah alamat untuk dirayapi dari hasil', dest='top', type=int, default=20)
# Menambahkan opsi untuk menentukan jumlah maksimum alamat yang diambil dari satu alamat
parser.add_argument('-l', '--limit', help='jumlah maksimum alamat yang diambil dari satu alamat', dest='limit', type=int, default=100)

# Parsing argumen dari input pengguna
args = parser.parse_args()

# Penjelasan singkat:
# - `-s` atau `--seeds`: Untuk menentukan alamat blockchain target.
# - `-o` atau `--output`: Untuk menentukan file output yang akan menyimpan data JSON mentah.
# - `-d` atau `--depth`: Untuk menentukan kedalaman perayapan, dengan nilai default 3.
# - `-t` atau `--top`: Untuk menentukan jumlah alamat yang akan dirayapi dari hasil, dengan nilai default 20.
# - `-l` atau `--limit`: Untuk menentukan jumlah maksimum alamat yang diambil dari satu alamat, dengan nilai default 100.


# Menyimpan argumen yang telah diparsing ke dalam variabel
top = args.top
seeds = args.seeds
depth = args.depth
limit = args.limit
output = args.output

# Menampilkan banner aplikasi
print ('''%s
┌┬┐┬─┐┌─┐┌┐┌┌─┐ ┌─┐┬ ┬┌─┐┬┌┐┌ ┌─┐┬─┐┌─┐┬ ┬┬  ┌─┐┬─┐
 │ ├┬┘├─┤│││└─┐ │  ├─┤├─┤││││ │  ├┬┘├─┤││││  ├┤ ├┬┘
 ┴ ┴└─┴ ┴┘└┘└─┘ └─┘┴ ┴┴ ┴┴┘└┘ └─┘┴└─┴ ┴└┴┘┴─┘└─┘┴└─
%s%s''' % (green, white, end))

# Inisialisasi database dan set untuk alamat yang telah diproses
database = {}
processed = set()

# Memecah alamat blockchain yang diberikan menjadi daftar
seeds = args.seeds.split(',')

# Menginisialisasi entri database untuk setiap alamat
for seed in seeds:
    database[seed] = {}

# Memulai proses mendapatkan data awal
getQuark()

# Fungsi untuk melakukan perayapan alamat blockchain
def crawl(addresses, processed, database, limit):
    # Menggunakan thread pool untuk menjalankan tugas perayapan secara paralel
    threadpool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    futures = (threadpool.submit(getTransactions, address, processed, database, limit) for address in addresses)
    for i, _ in enumerate(concurrent.futures.as_completed(futures)):
        print('%s Progress: %i/%i        ' % (info, i + 1, len(addresses)), end='\r')

try:
    for i in range(depth):
        # Menampilkan informasi level perayapan yang sedang berjalan
        print ('%s Crawling level %i' % (run, i + 1))
        # Menyusun ulang database berdasarkan ranking
        database = ranker(database, top + 1)
        # Mendapatkan alamat baru yang belum diproses
        toBeProcessed = getNew(database, processed)
        # Menampilkan jumlah alamat yang akan dirayapi
        print('%s %i addresses to crawl' % (info, len(toBeProcessed)))
        # Melakukan perayapan pada alamat yang belum diproses
        crawl(toBeProcessed, processed, database, limit)
except KeyboardInterrupt:
    pass

# Menyusun ulang database berdasarkan ranking akhir
database = ranker(database, top)

# Inisialisasi struktur JSON untuk menyimpan data node dan edge
jsoned = {'edges':[],'nodes':[]}
num = 1

num = 0
doneNodes = []
doneEdges = []
for node in database:
    x, y = genLocation()  # Menghasilkan lokasi acak untuk node
    size = len(database[node])
    if size > 20:
        size = 20
    if node not in doneNodes:
        doneNodes.append(node)
        jsoned['nodes'].append({'label': node, 'x': x, 'y': y, 'id':'id=' + node, 'size':size})
    for childNode in database[node]:
        uniqueSize = database[node][childNode]
        if uniqueSize > 20:
            uniqueSize = 20
        x, y = genLocation()
        if childNode not in doneNodes:
            doneNodes.append(childNode)
            jsoned['nodes'].append({'label': childNode, 'x': x, 'y': y, 'id':'id=' + childNode, 'size': uniqueSize})
        if (node + ':' + childNode or childNode + ':' + node) not in doneEdges:
            doneEdges.extend([(node + ':' + childNode), (childNode + ':' + node)])
            jsoned['edges'].append({'source':'id=' + childNode, 'target':'id=' + node, 'id':num, "size":uniqueSize/3 if uniqueSize > 3 else uniqueSize})
        num += 1

# Menampilkan jumlah dompet (nodes) dan koneksi (edges)
print('%s Total wallets:%i' % (info, len(jsoned['nodes'])))
print('%s Total connections:%i' % (info, len(jsoned['edges'])))

# Merender data ke dalam format JSON
render = json.dumps(jsoned).replace(' ', '').replace('\'', '"')

# Menyiapkan graf yang telah dihasilkan dalam file JSON
prepareGraph('%s.json' % seeds[0], render)
# Membuka hasil graf di browser
webbrowser.open('file://' + os.getcwd() + '/quark.html')

# Jika argumen output diberikan, simpan data ke file
if output:
    data = exporter(output, jsoned)
    new = open(output, 'w+')
    new.write(data)
    new.close()

# Mengakhiri program
quit()
