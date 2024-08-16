import sys
import os
import platform

colors = True # Menghasil kan Output
machine = sys.platform  # Mendeteksi os sistem saat ini
checkplatform = platform.platform() # Dapatkan versi OS saat ini
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False  # Warna tidak boleh ditampilkan di mac & windows
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    colors = True
    os.system('')   #Mengaktifkan ANSI
if not colors:
    end = red = white = green = yellow = run = bad = good = info = que = ''
else:
    white = '\033[97m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    end = '\033[0m'
    back = '\033[7;91m'
    info = '\033[93m[!]\033[0m'
    que = '\033[94m[?]\033[0m'
    bad = '\033[91m[-]\033[0m'
    good = '\033[92m[+]\033[0m'
    run = '\033[97m[~]\033[0m'
