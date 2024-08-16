"Secara keseluruhan program ini digunakan untuk memastikan bahwa file `quark.html`, yang diperlukan untuk menampilkan grafik, tersedia di direktori kerja saat ini."
import os
import shutil
from core.colors import bad, run, info

def getQuark():
     # Memeriksa apakah 'quark.html' ada dalam daftar file di direktori saat ini
	if 'quark.html' not in os.listdir():
        # Dapatkan direktory kerja saat ini
		cwd = os.getcwd()
        # Menampilkan pesan bahwa Quark diperlukan untuk melihat grafik yang dihasilkan
		print ('%s Quark diperlukan untuk melihat grafik yang dihasilkan.' % bad)
        # Menampilkan pesan bahwa proses pengunduhan alat sedang berlangsung
		print ('%s Downloading Quark [2.37 MB]' % run)
        # Menjalankan perintah untuk mengkloning repositori 'tols' dari GitHub secara diam-diam
		os.system('git clone https://github.com/s0md3v/Quark %s/Quark -q' % cwd)
        # Memindahkan folder 'libs' dari 'tols' ke direktori kerja saat ini
		os.system('mv ' + cwd + '/Quark/libs ' + cwd)
        # Memindahkan file 'tols.html' dari 'tols' ke direktori kerja saat ini
		os.system('mv ' + cwd + '/Quark/quark.html ' + cwd)
        # Menghapus file 'README.md' dari folder 'tols'
		os.remove(cwd + '/Quark/README.md')
        # Menghapus folder 'tols' setelah file yang diperlukan dipindahkan
		shutil.rmtree(cwd + '/Quark')
        #  Menampilkan pesan bahwa 'tols' telah diinstal dengan sukses
		print ('%s Quark Berhasil Diinstall' % info)
