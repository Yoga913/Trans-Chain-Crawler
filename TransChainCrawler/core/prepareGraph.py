"program ini digunakan untuk mempersiapkan visualisasi interaktif dari data dalam bentuk grafik yang akan ditampilkan di halaman web dengan cara otomatis tersetrukture."

import json
import random
# Fungsi untuk mempersiapkan grafik dan menyimpan data dalam format JSON dan JavaScript
def prepareGraph(filename, json_dump):
    # Membuat list kosong untuk node dan struktur JSON untuk node dan edge
    just_nodes = []
    jsoned = {'nodes': [], 'edges': []}

    data = 'var rendru = ' + json_dump
    savefile = open('%s.js' % filename, 'w+')
    savefile.write(data)
    savefile.close()
    # Membuka berkas HTML yang akan diubah untuk menyertakan skrip yang baru dibuat
    quark = open('quark.html', 'r')
    lines = quark.readlines()
    # Memodifikasi baris ke-7 dalam HTML untuk menyertakan skrip yang baru dibuat
    lines[6] = '<script id="ourfile" src="%s"></script>\n' % (filename + '.js')
    # Menyimpan kembali perubahan ke dalam berkas HTML
    with open('quark.html', 'w+') as quark_save:
        for line in lines:
            quark_save.write(line)

    quark.close()
